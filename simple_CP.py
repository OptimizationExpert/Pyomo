"""
================================================================================
 Title       : Simple CP Model
 Description : This OT-Tools code solves the a simple IP Problem

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""
from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.new_int_var(0, 2, f"x")
y = model.new_int_var(0, 2, f"y")
model.add(x + 5 * y <= 2)
model.maximize(x + y)
solver = cp_model.CpSolver()
results = solver.Solve(model)
print(solver.status_name(results))
print('OF =', solver.objective_value)
print(f'x ={solver.value(x)}, y= {solver.value(y)}')


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables: list[cp_model.IntVar]):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        print(f"Solution {self.__solution_count}")
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


class VarArraySolutionPrinternSolution(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables: list[cp_model.IntVar], n: int):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.__limit = n

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        print(f"Solution {self.__solution_count}")
        for v in self.__variables:
            print(f"{v}={self.value(v)}", end=" ")
        print()
        if self.__solution_count == self.__limit:
            self.stop_search()

    @property
    def solution_count(self) -> int:
        return self.__solution_count


def all_solutions_sample_sat():
    """Showcases calling the solver to search for small number of solutions."""
    # Creates the model.
    model = cp_model.CpModel()
    x = model.new_int_var(0, 2, f"x")
    y = model.new_int_var(0, 2, f"y")
    model.add(x + 5 * y <= 2)
    # model.maximize(x + y)
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinter([x, y])
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.solve(model, solution_printer)
    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


all_solutions_sample_sat()

print("----------------------------")


def all_solutions_sample_sat_nsolution():
    """Showcases calling the solver to search for small number of solutions."""
    # Creates the model.
    model = cp_model.CpModel()
    x = model.new_int_var(0, 2, f"x")
    y = model.new_int_var(0, 2, f"y")
    model.add(x + 5 * y <= 2)
    # model.maximize(x + y)
    solver = cp_model.CpSolver()
    solution_printer = VarArraySolutionPrinternSolution([x, y], 2)
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True
    # Solve.
    status = solver.solve(model, solution_printer)
    print(f"Status = {solver.status_name(status)}")
    print(f"Number of solutions found: {solution_printer.solution_count}")


all_solutions_sample_sat_nsolution()
