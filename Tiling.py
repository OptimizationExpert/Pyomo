"""
================================================================================
 Title       : <Tiling Puzzle>
 Description : This OT-Tools code solves the tiling puzzle

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from ortools.sat.python import cp_model

KOLORS = plt.cm.tab20(range(16))
cells = [
    (1, 1, 2),
    (1, 2, 1),
    (1, 3, 1),
    (1, 4, 2),
    (1, 5, 3),
    (2, 1, 1),
    (2, 2, 3),
    (2, 3, 0),
    (2, 4, 0),
    (2, 5, 1),
    (3, 1, 0),
    (3, 2, 0),
    (3, 3, 2),
    (3, 4, 2),
    (3, 5, 2),
    (4, 1, 3),
    (4, 2, 3),
    (4, 3, 0),
    (4, 4, 3),
    (4, 5, 1),
]

cells = [
    (1, 1, 2),
    (1, 2, 0),
    (1, 3, 1),
    (1, 4, 2),
    (1, 5, 1),
    (2, 1, 1),
    (2, 2, 3),
    (2, 3, 3),
    (2, 4, 3),
    (2, 5, 0),
    (3, 1, 2),
    (3, 2, 1),
    (3, 3, 0),
    (3, 4, 0),
    (3, 5, 2),
    (4, 1, 0),
    (4, 2, 1),
    (4, 3, 3),
    (4, 4, 3),
    (4, 5, 2),
]
values = range(4)
s_vals = []
s_dic = {}
s = 0
for i in values:
    for j in values:
        if (i, j) not in s_vals and (j, i) not in s_vals:
            s_vals.append((i, j))
            s += 1
            s_dic[s] = {i, j}
print(s_dic)
print(len(s_vals), s_vals)
nodes = {i: cells[i] for i in range(len(cells))}

neighbours = [(i, j) for i in nodes for j in nodes if
              i > j and abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1]) == 1]

model = cp_model.CpModel()
u = {(i, j, s): model.new_bool_var(f"u_{i}_{j}_{s}") for (i, j) in neighbours
     for s, set_vals in s_dic.items() if {nodes[i][2], nodes[j][2]} == set_vals}
print(u)

for s in s_dic:
    expr = [u[i, j, s] for (i, j) in neighbours if (i, j, s) in u]
    model.add_exactly_one(expr)

for (i, j, s1), v1 in u.items():
    for (ii, jj, s2), v2 in u.items():
        A = {i, j}
        B = {ii, jj}
        if A & B and A != B:
            model.add_at_most_one([v1, v2])

solver = cp_model.CpSolver()
# Solve.
status = solver.solve(model)
print(f"Status = {solver.status_name(status)}")

plt.figure()
for i in nodes:
    (x0, y0, v0) = nodes[i]
    width = 1
    height = 1
    rect = Rectangle(
        (x0 - 0.5, y0 - 0.5),
        width,
        height,
        fill=False,
        linewidth=2,
    )
    plt.gca().add_patch(rect)
    plt.text(x0, y0, s=str(nodes[i][2]), zorder=2, fontsize=10, fontweight="bold")
for s in s_dic:
    set_list = s_dic[s]
    f = lambda s: (s if s <= 5 else s - 5, 0 if s <= 5 else 1)
    p, m = f(s)
    plt.text(m + 5, p, s=str(set_list))

plt.xlim(0, 7)
plt.ylim(0, 7)
plt.xticks([])
plt.yticks([])
plt.tight_layout()
plt.savefig("Tiling_0.png")
for ss in range(1,11):

    for (i, j, s), v in u.items():
        if solver.value(v) > 0 and s==ss:
            (x0, y0, v0) = nodes[i]
            (x1, y1, v1) = nodes[j]
            rect1 = Rectangle(
                (x0 - 0.5, y0 - 0.5),
                width,
                height,
                fill=True,
                linewidth=2,
                facecolor=KOLORS[s],
                alpha=0.5,
            )
            rect2 = Rectangle(
                (x1 - 0.5, y1 - 0.5),
                width,
                height,
                fill=True,
                linewidth=2,
                facecolor=KOLORS[s],
                alpha=0.5,
            )
            plt.gca().add_patch(rect1)
            plt.gca().add_patch(rect2)
            set_list = s_dic[s]
            f = lambda s: (s if s <= 5 else s - 5, 0 if s <= 5 else 1)
            p, m = f(s)
            plt.text(m + 5, p, s=str(set_list), c='b')
            plt.tight_layout()
            plt.savefig(f"Tiling_{s}.png")

plt.show()
