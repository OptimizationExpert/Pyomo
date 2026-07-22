import matplotlib.pyplot as plt
from ortools.sat.python import cp_model

st, fn, N = 98, 58, 10
st, fn, N = 98, 58, 10
st, fn, N = 16, 19, 6
st, fn, N = 25, 13, 6

grid = {}
c = 0
for i in range(N):
    for j in range(N):
        c += 1
        grid[c] = (i, j)

for c, (i, j) in grid.items():
    plt.scatter(i, j, s=20)
    plt.text(i, j, s=str(c) + ' ' + f"{i}-{j}")
plt.axis('off')

nodes = [c for c in grid.keys()]
connect = {(c1, c2) for c1 in nodes for c2 in nodes if
           abs(grid[c1][0] - grid[c2][0]) + abs(grid[c1][1] - grid[c2][1]) == 1}
plt.show()

model = cp_model.CpModel()
solver = cp_model.CpSolver()
numbers = [n for n in range(N)]
non_snake_numbers = [n for n in range(1, N)]
cell_assign = {(i, n): model.new_bool_var(f"assign_to_number_{i}_{n}") for i in nodes for n in numbers}
U = {(i, j): model.new_bool_var(f"connection_{i}_{j}") for i in nodes for j in nodes if (i, j) in connect}
snake = {i: cell_assign[i, 0] for i in nodes}

flow_n = {(i, j, n): model.new_int_var(0, n - 1, f"flow_{i}_{j}_{n}") for i in nodes for j in nodes for n in
          non_snake_numbers if
          (i, j) in connect}
source_n = {(i, n): model.new_bool_var(f"source_{i}_{n}") for i in nodes for n in non_snake_numbers}

arcs = [(i, j, v) for (i, j), v in U.items()] + [(i, i, v.Not()) for i, v in snake.items()]
arcs += [(st, fn, True)]
model.add_circuit(arcs)

for (i, n), v in cell_assign.items():
    if n in non_snake_numbers:
        model.add(source_n[i, n] <= v)
for i in nodes:
    expr = [cell_assign[i, n] for n in numbers]
    model.add_exactly_one(expr)

for n in non_snake_numbers:
    expr_assign = [cell_assign[i, n] for i in nodes]
    model.add(sum(expr_assign) == n)
    expr_src = [source_n[i, n] for i in nodes]
    model.add_exactly_one(expr_src)
for i in nodes:
    for n in non_snake_numbers:
        out_flow = sum([flow_n[i, j, n] for j in nodes if (i, j, n) in flow_n])
        in_flow = sum([flow_n[j, i, n] for j in nodes if (j, i, n) in flow_n])
        model.add(n * source_n[i, n] - cell_assign[i, n] == out_flow - in_flow).only_enforce_if(cell_assign[i, n])

for (i, j, n), v in flow_n.items():
    model.add(v <= n * cell_assign[i, n])
    model.add(v <= n * cell_assign[j, n])

model.add(cell_assign[fn, 0] == True)
model.add(cell_assign[st, 0] == True)
for n in non_snake_numbers:
    model.add(cell_assign[fn, n] == False)
    model.add(cell_assign[st, n] == False)

# Maximize x
expressions = [v for (i, j), v in U.items()]
model.minimize(sum(expressions))

status = solver.Solve(model)
print(solver.status_name(status))

plt.figure()
for c, (i, j) in grid.items():
    plt.scatter(i, j, s=20)
for (i, j), v in U.items():
    if solver.value(v) > 0:
        (x0, y0) = grid[i]
        (x1, y1) = grid[j]
        plt.plot([x0, x1], [y0, y1], c='k')
for (i, n), v in cell_assign.items():
    if solver.value(v) > 0:
        (x0, y0) = grid[i]
        plt.text(x0, y0, str(n))
for (i, n), v in source_n.items():
    if solver.value(v) > 0:
        (x0, y0) = grid[i]
        plt.scatter(x0, y0, s=200, alpha=0.5)
plt.axis('off')
plt.show()

KOLOR = ['grey', 'red', 'blue', 'green', 'gold', 'brown',
         'dodgerblue', 'cyan', 'magenta', 'orange', 'purple', 'black']

fig, ax = plt.subplots(figsize=(5, 5))
for n in [0]:
    for i in nodes:
        x0, y0 = grid[i]
        square = plt.Rectangle((x0 + .5, y0 + 0.5), 1, 1, fill=True, linewidth=2, facecolor=KOLOR[n],
                               edgecolor='purple', alpha=0.3)
        ax.add_patch(square)
for i in [fn, st]:
    x0, y0 = grid[i]
    plt.scatter(x0 + 1, y0 + 1, s=200, c='r', alpha=1, zorder=2)

plt.xticks(range(1, 1 + N))
plt.yticks(range(1, 1 + N))

ax.set_xlim(0.5, N + 0.5)
ax.set_ylim(0.5, N + 0.5)
ax.set_aspect('equal')
ax.grid(True)
plt.title("Square")
plt.show()

fig, ax = plt.subplots(figsize=(5, 5))
for n in numbers:
    for i in nodes:
        if solver.value(cell_assign[i, n]) > 0:
            x0, y0 = grid[i]
            square = plt.Rectangle((x0 + .5, y0 + 0.5), 1, 1, fill=True, linewidth=2, facecolor=KOLOR[n],
                                   edgecolor='purple', alpha=0.3)
            ax.add_patch(square)

for (i, j), v in U.items():
    if solver.value(v) > 0:
        (x0, y0) = grid[i]
        (x1, y1) = grid[j]
        plt.plot([x0 + 1, x1 + 1], [y0 + 1, y1 + 1], c='k', lw=2)

for i in [fn, st]:
    x0, y0 = grid[i]
    plt.scatter(x0 + 1, y0 + 1, s=200, c='r', alpha=1, zorder=2)
ax.set_xlim(0.5, N + 0.5)
ax.set_ylim(0.5, N + 0.5)
ax.set_aspect('equal')
ax.grid(True)
plt.xticks(range(1, 1 + N))
plt.yticks(range(1, 1 + N))
plt.title("Square")
plt.show()
