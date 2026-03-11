# data is taken from this repo https://github.com/ctbo/slitherlink
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model  # CP-SAT solver
from base import Node, Cell
from tools import make_data, dist, neighbour
"""
Slitherlink (also known as Fences and Loop the Loop) is a logic puzzle with simple rules and challenging solutions.
The rules are simple. You have to draw lines between the dots to form a single loop without crossings or branches. The numbers indicate how many lines surround it.

Solved by alireza.soroudi@gmail.com
"""

file_name = "test5.txt"
file_name = "test30x45.txt"
file_name = "test30x20.txt"
with open(file_name, "r") as f:
    puzzle_text = f.read().strip()  # keeps newlines, removes leading/trailing whitespace

data_dict = make_data(puzzle_text)
rows = data_dict["rows"]
cols = data_dict["cols"]
nodes = data_dict["nodes"]
cells = data_dict["cells"]


cells_all = []
nodes_all = []
for n in nodes:
    nodes_all.append(
        Node(name=n,
             position=nodes[n]
             )
    )
node_by_id = {n.name: n for n in nodes_all}

for i, c in cells.items():
    cells_all.append(
        Cell(name=i,
             position=c['position'],
             nodes=[node_by_id[n] for n in c['nodes']],
             value=c['value']
             )
    )

plt.figure()
for n in nodes_all:
    x, y = n.position
    plt.scatter(x, y, s=5, c='k')
for c in cells_all:
    x, y = c.position
    nodes_in_cell = [n.name for n in c.nodes]
    xm = sum([node.position[0] for node in c.nodes]) / len(c.nodes)
    ym = -0.2 + sum([node.position[1] for node in c.nodes]) / len(c.nodes)
    if c.value:
        plt.text(xm, ym, s=str(c.value), fontsize=8)

model = cp_model.CpModel()
solver = cp_model.CpSolver()

U = {(i.name, j.name): model.NewBoolVar(f"connection_{i.name}_{j.name}") for i in nodes_all for j in nodes_all if
     neighbour(i, j)}
selected = {i.name: model.NewBoolVar(f"select_{i.name}") for i in nodes_all}

arcs = [(i, j, v) for (i, j), v in U.items()] + [(i, i, v.Not()) for i, v in selected.items()]
model.AddCircuit(arcs)

for cell in cells_all:
    nodes_in_cell = [n.name for n in cell.nodes]
    around_expr = [v for (i, j), v in U.items() if i in nodes_in_cell and j in nodes_in_cell]
    if cell.value is not None:
        model.Add(sum(around_expr) == cell.value)

# Maximize x
expressions = [v * dist(i, j, node_by_id) for (i, j), v in U.items()]
# model.Minimize(sum(expressions))
status = solver.Solve(model)
print(solver.status_name(status), solver.objective_value)

for (i, j), v in U.items():
    if i > j:
        x0, y0 = node_by_id[i].position
        x1, y1 = node_by_id[j].position
        if solver.value(v) + solver.value(U[j, i]) == 1:
            plt.plot([x0, x1], [y0, y1], c='r', lw=2)
        else:
            plt.plot([x0, x1], [y0, y1], c='k', lw=0.5, alpha=0.5)

plt.tight_layout()
plt.axis('off')
plt.show()
