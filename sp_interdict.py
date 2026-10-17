#  Based on the Pyomo shortest path interdiction example (Sandia, BSD license).
#  Updated for modern pandas (no .ix) and Pyomo (no reconstruct/preprocess internals).

import logging

import pandas as pd
import pyomo.environ as pe
from pyomo.opt import SolverStatus, TerminationCondition


class SPInterdiction:
    """Shortest path interdiction.

    nodefile columns: Node, SupplyDemand   (negative = supply, positive = demand)
    arcfile  columns: StartNode, EndNode, Cost, Attackable
    """

    def __init__(self, nodefile, arcfile, attacks=0, solver="appsi_highs", solver_path=None):
        self.node_data = pd.read_csv(nodefile).set_index("Node").sort_index()
        self.arc_data = pd.read_csv(arcfile).set_index(["StartNode", "EndNode"]).sort_index()

        self.node_set = list(self.node_data.index)
        self.arc_set = list(self.arc_data.index)
        self.nCmax = len(self.node_set) * self.arc_data["Cost"].max()

        self.solver = (pe.SolverFactory(solver, executable=solver_path) if solver_path
                       else pe.SolverFactory(solver))

        self.createPrimal()
        self.createInterdictionDual()
        self.attacks = attacks

    # Budget is a mutable Param, so changing it does not require rebuilding the model
    @property
    def attacks(self):
        return int(pe.value(self.Idual.budget))

    @attacks.setter
    def attacks(self, k):
        self.Idual.budget.set_value(k)

    def createPrimal(self):
        """Min-cost flow after interdiction; interdicted arcs get a large penalty xbar."""
        m = pe.ConcreteModel()
        m.node_set = pe.Set(initialize=self.node_set)
        m.edge_set = pe.Set(initialize=self.arc_set, dimen=2)

        m.xbar = pe.Param(m.edge_set, initialize=0, mutable=True)
        m.y = pe.Var(m.edge_set, domain=pe.NonNegativeReals)
        m.UnsatSupply = pe.Var(m.node_set, domain=pe.NonNegativeReals)
        m.UnsatDemand = pe.Var(m.node_set, domain=pe.NonNegativeReals)

        big = 2 * self.nCmax + 1
        cost = self.arc_data["Cost"]
        m.OBJ = pe.Objective(
            expr=sum((cost[e] + m.xbar[e] * big) * m.y[e] for e in m.edge_set)
            + sum(self.nCmax * (m.UnsatSupply[n] + m.UnsatDemand[n]) for n in m.node_set),
            sense=pe.minimize)

        def flow_bal_rule(m, n):
            inflow = sum(m.y[i, j] for (i, j) in m.edge_set if j == n)
            outflow = sum(m.y[i, j] for (i, j) in m.edge_set if i == n)
            imb = self.node_data.at[n, "SupplyDemand"]
            rhs = imb
            if imb < 0:
                rhs = rhs + m.UnsatSupply[n]
            if imb > 0:
                rhs = rhs - m.UnsatDemand[n]
            return inflow - outflow == rhs

        m.FlowBalance = pe.Constraint(m.node_set, rule=flow_bal_rule)
        self.primal = m

    def createInterdictionDual(self):
        """Max over interdictions of the dual of the shortest path problem (a MILP)."""
        m = pe.ConcreteModel()
        m.node_set = pe.Set(initialize=self.node_set)
        m.edge_set = pe.Set(initialize=self.arc_set, dimen=2)

        m.budget = pe.Param(initialize=0, mutable=True, within=pe.NonNegativeIntegers)
        m.rho = pe.Var(m.node_set, domain=pe.Reals)
        m.x = pe.Var(m.edge_set, domain=pe.Binary)

        m.OBJ = pe.Objective(
            expr=sum(self.node_data.at[n, "SupplyDemand"] * m.rho[n] for n in m.node_set),
            sense=pe.maximize)

        big = 2 * self.nCmax + 1

        def edge_rule(m, i, j):
            att = int(self.arc_data.at[(i, j), "Attackable"])
            return m.rho[j] - m.rho[i] <= self.arc_data.at[(i, j), "Cost"] + big * m.x[i, j] * att

        m.DualEdgeConstraint = pe.Constraint(m.edge_set, rule=edge_rule)

        def unsat_rule(m, n):
            imb = self.node_data.at[n, "SupplyDemand"]
            if imb < 0:
                return -m.rho[n] <= self.nCmax
            if imb > 0:
                return m.rho[n] <= self.nCmax
            return pe.Constraint.Skip

        m.UnsatConstraint = pe.Constraint(m.node_set, rule=unsat_rule)
        m.BlockLimit = pe.Constraint(expr=pe.summation(m.x) <= m.budget)
        self.Idual = m

    def _solve(self, model, tee):
        res = self.solver.solve(model, tee=tee)
        if res.solver.status != SolverStatus.ok:
            logging.warning("Solver status not ok")
        if res.solver.termination_condition != TerminationCondition.optimal:
            logging.warning("Solution not proven optimal")

    def solve(self, tee=False):
        self._solve(self.Idual, tee)
        for e in self.arc_set:
            self.primal.xbar[e] = round(pe.value(self.Idual.x[e]))
        self._solve(self.primal, tee)

    def printSolution(self):
        print(f"\nUsing {self.attacks} attacks:\n")
        for e in sorted(self.arc_set):
            if pe.value(self.Idual.x[e]) > 0.5:
                print(f"Interdict arc {e[0]} -> {e[1]}")
        print()
        for n in sorted(self.node_set):
            if pe.value(self.primal.UnsatSupply[n]) > 1e-6:
                print(f"Remaining supply on node {n}: {pe.value(self.primal.UnsatSupply[n]):.2f}")
            if pe.value(self.primal.UnsatDemand[n]) > 1e-6:
                print(f"Remaining demand on node {n}: {pe.value(self.primal.UnsatDemand[n]):.2f}")
        for e in self.arc_set:
            if pe.value(self.primal.y[e]) > 1e-6:
                print(f"Flow on arc {e[0]} -> {e[1]}: {pe.value(self.primal.y[e]):.2f}")
        print("----------")
        print(f"Total cost = {pe.value(self.primal.OBJ):.2f} (primal) {pe.value(self.Idual.OBJ):.2f} (dual)")


if __name__ == "__main__":
    # Needs a MILP solver: appsi_highs (pip install highspy), cbc, glpk, gurobi, ...
    # Example with an executable: SPInterdiction(..., solver="cbc", solver_path=r"C:\cbc\bin\cbc.exe")
    m = SPInterdiction("sample_nodes_data.csv", "sample_arcs_data.csv")
    for k in (0, 1, 2):
        m.attacks = k
        m.solve()
        m.printSolution()