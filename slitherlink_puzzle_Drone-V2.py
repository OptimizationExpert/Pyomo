# data is taken from this repo https://github.com/ctbo/slitherlink
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model  # CP-SAT solver
from base import Node, Cell
from tools import make_data, neighbour

"""
Slitherlink (also known as Fences and Loop the Loop) is a logic puzzle with simple rules and challenging solutions.
The rules are simple. You have to draw lines between the dots to form a single loop without crossings or branches. The numbers indicate how many lines surround it.

Solved by alireza.soroudi@gmail.com
"""
KOLORS = ['b', 'gold', 'r', 'brown', 'green', 'k']

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
        Cell(name=int(i),
             position=c['position'],
             nodes=[node_by_id[n] for n in c['nodes']],
             value=c['value']
             )
    )
Ndr = 5
drones = [d for d in range(Ndr)]
depot_ids = [1, 13, 7]
depot_ids = [1, 100, 300]

#depot_ids = [1, 295, 613, 300, 200]
# depot_ids = [1, 295, 613]

# depots = [n for i, n in node_by_id.items() if i in depot_ids]

plt.figure(figsize=(10, 8))
for n in nodes_all:
    x, y = n.position
    plt.scatter(x, y, s=20, c='k')
    plt.text(x, y, s=str(n.name), c='b')

cell_by_ids = {c.name: c for c in cells_all}

for c in cells_all:
    x, y = c.position
    nodes_in_cell = [n.name for n in c.nodes]
    xm = sum([node.position[0] for node in c.nodes]) / len(c.nodes)
    ym = -0.2 + sum([node.position[1] for node in c.nodes]) / len(c.nodes)
    if c.value:
        plt.text(xm, ym, s=str(c.value), fontsize=8, fontweight='bold')

model = cp_model.CpModel()
solver = cp_model.CpSolver()

U = {(i.name, j.name, dr): model.new_bool_var(f"connection_{i.name}_{j.name}_{dr}") for i in nodes_all for j in nodes_all
     for dr in drones if
     neighbour(i, j)}
selected = {(i.name, dr): model.new_bool_var(f"select_{i.name}_{dr}") for i in nodes_all for dr in drones}
drone_used = {dr: model.new_bool_var(f"drone_{dr}") for dr in drones}
ctodr = {(cell.name, dr): model.new_bool_var(f"cell_{cell.name}_drone_{dr}") for cell in cells_all for dr in drones if
         cell.value is not None}
print("U", len(U))
print("selected", len(selected))
print("drone_used", len(drone_used))
print("ctodr", len(ctodr))

for (i, j, dr), v in U.items():
    model.add(v <= drone_used[dr])
for (i, dr), v in selected.items():
    model.add(v <= drone_used[dr])

for cell in cells_all:
    if cell.value is not None:
        expr = [ctodr[cell.name, dr] for dr in drones]
        model.add_exactly_one(expr)
        for dr in drones:
            model.add(ctodr[cell.name, dr] <= drone_used[dr])

for dr in drones:
    expr = [selected[d, dr] for d in depot_ids]
    model.add(sum(expr)>= drone_used[dr])
    #model.add(sum(expr)<= drone_used[dr]*len(depot_ids))

    arcs = [(i, j, v) for (i, j, ddr), v in U.items() if ddr == dr] + [(i, i, v.Not()) for (i, ddr), v in
                                           selected.items() if ddr == dr]
    model.add_circuit(arcs)
    travelled_arcs = [v for (i, j, ddr), v in U.items() if ddr == dr]
    model.add( cp_model.LinearExpr.sum(travelled_arcs) <= 360*drone_used[dr])
for cell in cells_all:
    for dr in drones:
        nodes_in_cell = [n.name for n in cell.nodes]
        #around_expr = [v for (i, j, ddr), v in U.items() if i in nodes_in_cell and j in nodes_in_cell and ddr == dr]
        around_expr = [v for (i, ddr), v in selected.items() if i in nodes_in_cell and ddr == dr]
        if cell.value is not None:
            # print('XXXX', cell.name, cell.value, len(around_expr),nodes_in_cell)
            # pass
            model.add(cp_model.LinearExpr.sum(around_expr) >= cell.value * ctodr[cell.name, dr])

solver.parameters.max_time_in_seconds = 200
solver.parameters.log_search_progress = False
expressions = [v for (i, j, dr), v in U.items()]
#model.minimize(cp_model.LinearExpr.sum(expressions))

status = solver.Solve(model)
print(solver.status_name(status), solver.objective_value)


for (i, j, dr), v in U.items():
    if i > j:
        x0, y0 = node_by_id[i].position
        x1, y1 = node_by_id[j].position
        plt.plot([x0, x1], [y0, y1], '--k', lw=0.5, alpha=0.5)
plt.tight_layout()
plt.axis('off')
plt.savefig('base_slitherlink.png')
"""
for (c,dr),v in ctodr.items():
    if solver.value(v):
        print('ctodr',c,dr,cell_by_ids[c].value )
        print([n.name for n in cell_by_ids[c].nodes])
"""

for dr, v in drone_used.items():
    if solver.value(v):
        print("drone_used", dr)
for (i, j, dr), v in U.items():
    if i != j:
        x0, y0 = node_by_id[i].position
        x1, y1 = node_by_id[j].position
        if solver.value(v) + solver.value(U[j, i, dr]) > 0:
            plt.plot([x0, x1], [y0, y1], c=KOLORS[dr], lw=3)
        else:
            plt.plot([x0, x1], [y0, y1], c='k', lw=0.5, alpha=0.5)

for i in node_by_id:
    if i in depot_ids:
        x0, y0 = node_by_id[i].position
        plt.scatter(x0, y0, s=100, marker='s')

plt.tight_layout()
plt.axis('off')
plt.savefig('final_slitherlink.png')

for cell in cells_all:
    for dr in drones:
        nodes_in_cell = [n.name for n in cell.nodes]
        around_expr_v = [solver.value(v) for (i, j, ddr), v in U.items() if
                         i in nodes_in_cell and j in nodes_in_cell and ddr == dr]
        around_expr = [(i, j, ddr) for (i, j, ddr), v in U.items() if
                       i in nodes_in_cell and j in nodes_in_cell and ddr == dr]
        if cell.name == 30 and cell.value is not None and solver.value(ctodr[cell.name, dr]) > 0:
            print('XXXX', cell.name, cell.value, dr, nodes_in_cell)
            print(around_expr_v)
            print(around_expr)

            # pass
            # model.Add(cp_model.LinearExpr.sum(around_expr) >= cell.value ).only_enforce_if(ctodr[cell.name, dr])

plt.show()
