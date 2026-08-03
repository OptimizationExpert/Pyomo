"""
Developed by Alireza Soroudi
Constraint programming in ORTools
alireza.soroudi@gmail.com
puzzle source: project 18,67
https://projecteuler.net/problem=67

"""
from matplotlib import pyplot as plt
from ortools.sat.python import cp_model

data = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

rows = [r for r in range(len(data))]
cols = [len(data[r]) for r in rows]
col_max = max(cols)
n = 0
dic_data = {}
for r in rows:
    for c, v in enumerate(data[r]):
        n += 1
        dic_data[n] = (r, c, v)
dic_by_loc = {(r, c): n for n, (r, c, v) in dic_data.items()}

nodes = [i for i in range(1, n + 1)]
neighbour = {}
for n in nodes:
    (r, c, v) = dic_data[n]
    neighbour[n] = []
    if r + 1 in rows:
        cols = [j for j in range(len(data[r + 1]))]
        if c + 1 in cols:
            neighbour[n].append(dic_by_loc[r + 1, c + 1])
        if c in cols:
            neighbour[n].append(dic_by_loc[r + 1, c])

print(neighbour)
rowmax = max(rows)
model = cp_model.CpModel()
x = {(i, j): model.new_bool_var(f"flow_{i}_{j}") for i in nodes
     for j in nodes if i in neighbour and j in neighbour[i]}

fn = {i: model.new_bool_var(f"fn_{i}") for i in nodes if dic_data[i][0] == rowmax}
select = {i: model.new_bool_var(f"select_{i}") for i in nodes}

arcs = [(i, j, v) for (i, j), v in x.items()] + [(j, 1, v_link) for j, v_link in fn.items()] + [(i, i, v.Not()) for i, v
                                                                                                in select.items()]
model.add_circuit(arcs)

for (i, j), v in x.items():
    model.add(v <= select[i])
    model.add(v <= select[j])

expr_fn = [v_link for j, v_link in fn.items()]
model.add_exactly_one(expr_fn)

expr_fn_select = [select[j] for j, v_link in fn.items()]
model.add_exactly_one(expr_fn_select)
for j, v_link in fn.items():
    model.add(v_link <= select[j])

expr = [v * dic_data[i][2] for i, v in select.items()]
model.maximize(sum(expr))

solver = cp_model.CpSolver()
results = solver.Solve(model)
print(solver.status_name(results))
print('OF = ', solver.best_objective_bound)
plt.figure(figsize=(5, 5))

for n, (r, c, v) in dic_data.items():
    bias = 0.5 * col_max + 0.5 - 0.5 * r
    plt.scatter(bias + c, rowmax - r, s=220, c='grey', alpha=0.4, zorder=0)
    # plt.text(bias + c - 0.2, rowmax - r - 0.7, s=str(n))
    plt.text(bias + c - 0.2, rowmax - r - 0.1, s=str(v), fontweight='bold')

for (i, j), v in x.items():
    if solver.Value(v) > 0:
        r0, c0, v0 = dic_data[i]
        r1, c1, v1 = dic_data[j]
        bias0 = 0.5 * col_max + 0.5 - 0.5 * r0
        bias1 = 0.5 * col_max + 0.5 - 0.5 * r1

        x0, y0 = bias0 + c0, rowmax - r0
        x1, y1 = bias1 + c1, rowmax - r1

        plt.plot([x0, x1], [y0, y1], lw=3, color='r', zorder=1)
plt.axis('off')
plt.tight_layout()
plt.show()



plt.figure(figsize=(5, 5))

for n, (r, c, v) in dic_data.items():
    bias = 0.5 * col_max + 0.5 - 0.5 * r
    plt.scatter(bias + c, rowmax - r, s=220, c='grey', alpha=0.4, zorder=0)
    plt.text(bias + c - 0.2, rowmax - r - 0.1, s=str(v), fontweight='bold')
plt.axis('off')
plt.tight_layout()

for r in rows:
    for (i, j), v in x.items():
        if solver.Value(v) > 0:
            r0, c0, v0 = dic_data[i]
            r1, c1, v1 = dic_data[j]
            bias0 = 0.5 * col_max + 0.5 - 0.5 * r0
            bias1 = 0.5 * col_max + 0.5 - 0.5 * r1

            x0, y0 = bias0 + c0, rowmax - r0
            x1, y1 = bias1 + c1, rowmax - r1
            if r0==r:
                plt.plot([x0, x1], [y0, y1], lw=3, color='r', zorder=1)
                plt.savefig(f"row {r}.png")
plt.show()
