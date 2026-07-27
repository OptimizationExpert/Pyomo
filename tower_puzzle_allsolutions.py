"""
Developed by Alireza Soroudi
alireza.soroudi@gmail.com
The Tower Puzzle:
data and some functions related to data is taken from https://github.com/niloufarmtd/Skyscraper-Puzzle-Solver
is a classic Japanese-style logic puzzle where you fill an N×N grid with buildings of varying heights, using only the edge clues and pure deduction — no guessing required. Every row and every column contains each height from 1 to N exactly once, and the numbers around the perimeter tell you how many buildings are visible from that side.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import re

from ortools.sat.python import cp_model

PUZZLE = """
   5  4  2  3  1  2  3  4  4
4 [1, 2, 7, 5, 9, 8, 6, 4, 3] 5
3 [3, 4, 9, 7, 2, 1, 8, 6, 5] 4
3 [5, 6, 2, 9, 4, 3, 1, 8, 7] 3
4 [2, 3, 8, 6, 1, 9, 7, 5, 4] 4
2 [8, 9, 5, 3, 7, 6, 4, 2, 1] 6
3 [7, 8, 4, 2, 6, 5, 3, 1, 9] 1
3 [6, 7, 3, 1, 5, 4, 2, 9, 8] 2
1 [9, 1, 6, 4, 8, 7, 5, 3, 2] 6
4 [4, 5, 1, 8, 3, 2, 9, 7, 6] 3
   2  4  4  2  3  3  1  2  3
"""

# PUZZLE =
"""  2  1  2
2 [1, 3, 2] 2
1 [3, 2, 1] 3
2 [2, 1, 3] 1
   2  3  1"""

#PUZZLE =
"""3  2  1  2
3 [1, 3, 4, 2] 2
2 [3, 1, 2, 4] 1
2 [2, 4, 1, 3] 2
1 [4, 2, 3, 1] 3
   1  2  2  3"""


def parse_skyscrapers(text):
    """-> (grid, clues) where clues has keys 'top','bottom','left','right'."""
    lines = [ln for ln in text.strip().splitlines() if ln.strip()]

    top = [int(v) for v in lines[0].split()]
    bottom = [int(v) for v in lines[-1].split()]

    grid, left, right = [], [], []
    for ln in lines[1:-1]:
        head, body, tail = re.match(r"\s*(\d+)\s*\[([^\]]*)\]\s*(\d+)\s*", ln).groups()
        left.append(int(head))
        right.append(int(tail))
        grid.append([int(v) for v in body.replace(",", " ").split()])

    n = len(grid)
    assert all(len(r) == n for r in grid), "grid is not square"
    assert len(top) == len(bottom) == len(left) == len(right) == n, "clue count != n"

    return {"top": top, "bottom": bottom, "left": left, "right": right}


clues = parse_skyscrapers(PUZZLE)
print(clues)


def create_grid(N):
    grid = {}
    c = 0
    for i in range(N):
        for j in range(N):
            c += 1
            grid[c] = (i, j)
    return grid


N = len(clues['top'])
grid = create_grid(N)
print(grid)
cells = [c for c in grid]


class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        super().__init__()
        self._variables = variables
        self._solution_count = 0
        self.last = None
        self.collector = {}

    def on_solution_callback(self) -> None:
        self._solution_count += 1
        self.last = {c: self.value(v) for c, v in self._variables.items()}
        print(f"--- solution {self._solution_count} ---")
        #for c, v in self._variables.items():
        #    print(f"{c}={self.value(v)}", end=" ")
        self.collector[self._solution_count] = self.last
        print()
        if self._solution_count > 10:
            self.StopSearch()

    @property
    def solution_count(self) -> int:
        return self._solution_count


def tower(N):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    rows = [r for r in range(N)]
    cols = [c for c in range(N)]

    u = {c: model.new_int_var(1, N, f"Number_{c}") for c in cells}
    visible = {(c, d): model.new_bool_var(f"visible_{c}_{d}") for c in cells for d in clues}

    compare = {(c1, c2): model.new_bool_var(f"compare_{c1}_{c2}") for c1 in cells for c2 in cells
               if c1 > c2 and (grid[c1][0] == grid[c2][0] or grid[c1][1] == grid[c2][1])
               }
    compare.update({(c2, c1): v.Not() for (c1, c2), v in compare.items()})

    for row in rows:
        expr = [u[c] for c in cells if grid[c][1] == row]
        model.add_all_different(expr)
    for col in cols:
        expr = [u[c] for c in cells if grid[c][0] == col]
        model.add_all_different(expr)

    for col in cols:
        for d in ['top', 'bottom', 'left', 'right']:
            for row in rows:
                for c in cells:
                    if d == 'top' and grid[c][0] == col and grid[c][1] == row:
                        if grid[c][1] == N - 1:
                            model.add(visible[c, d] == 1)
                        else:
                            expr_v = [compare[c, cc] for cc in cells if grid[cc][1] > row and grid[cc][0] == col]
                            model.add(sum(expr_v) == len(expr_v)).only_enforce_if(visible[c, d])
                            expr_nv = [v.Not() for v in expr_v]
                            model.add_at_least_one(expr_nv).only_enforce_if(visible[c, d].Not())
                    if d == 'bottom' and grid[c][0] == col and grid[c][1] == row:
                        if grid[c][1] == 0:
                            model.add(visible[c, d] == 1)
                        else:
                            expr_v = [compare[c, cc] for cc in cells if grid[cc][1] < row and grid[cc][0] == col]
                            model.add(sum(expr_v) == len(expr_v)).only_enforce_if(visible[c, d])
                            expr_nv = [v.Not() for v in expr_v]
                            model.add_at_least_one(expr_nv).only_enforce_if(visible[c, d].Not())
                    if d == 'left' and grid[c][0] == col and grid[c][1] == row:
                        if grid[c][0] == 0:
                            model.add(visible[c, d] == 1)
                        else:
                            expr_v = [compare[c, cc] for cc in cells if grid[cc][0] < col and grid[cc][1] == row]
                            model.add(sum(expr_v) == len(expr_v)).only_enforce_if(visible[c, d])
                            expr_nv = [v.Not() for v in expr_v]
                            model.add_at_least_one(expr_nv).only_enforce_if(visible[c, d].Not())
                    if d == 'right' and grid[c][0] == col and grid[c][1] == row:
                        if grid[c][0] == N - 1:
                            model.add(visible[c, d] == 1)
                        else:
                            expr_v = [compare[c, cc] for cc in cells if grid[cc][0] > col and grid[cc][1] == row]
                            expr_c = [cc for cc in cells if grid[cc][0] > col and grid[cc][1] == row]
                            model.add(sum(expr_v) == len(expr_v)).only_enforce_if(visible[c, d])
                            expr_nv = [v.Not() for v in expr_v]
                            model.add_at_least_one(expr_nv).only_enforce_if(visible[c, d].Not())

    for (c1, c2), v in compare.items():
        model.add(u[c1] > u[c2]).only_enforce_if(v)
        model.add(u[c1] < u[c2]).only_enforce_if(v.Not())

    for d in ['top', 'bottom']:
        for col in cols:
            expr = [visible[c, d] for c in cells if grid[c][0] == col]
            model.add(sum(expr) == clues[d][col])

    for d in ['left', 'right']:
        for row in rows:
            expr = [visible[c, d] for c in cells if grid[c][1] == row]
            model.add(sum(expr) == clues[d][N - row - 1])

    solver.parameters.enumerate_all_solutions = True
    solution_printer = VarArraySolutionPrinter(u)
    status = solver.Solve(model, solution_printer)
    print(solver.status_name(status))
    return solver, u, solution_printer.collector


solver, u, collector = tower(N)

print(collector)


def shades(n, base="YlOrBr", lo=0.15, hi=0.92, gamma=1.0):
    """List of n RGBA colours; shades(n)[v - 1] is the colour for value v."""
    t = np.linspace(0.0, 1.0, n) ** gamma
    return plt.get_cmap(base)(lo + t * (hi - lo))


def readable(rgba, threshold=0.55):
    r, g, b = rgba[:3]
    return "#2C2C2A" if 0.299 * r + 0.587 * g + 0.114 * b > threshold else "#FFFFFF"


def draw_rect(ax, x, y, value, n, w=1.0, h=1.0, palette=None,
              label=True, edge="white", lw=1.5, radius=0.0):
    """Rectangle with lower-left corner at (x, y), shaded by `value` in 1..n.

    Returns the RGBA colour used.
    """
    if palette is None:
        palette = shades(n)
    color = palette[int(value) - 1]

    if radius:
        from matplotlib.patches import FancyBboxPatch
        patch = FancyBboxPatch(
            (x + radius, y + radius), w - 2 * radius, h - 2 * radius,
            boxstyle=f"round,pad={radius}",
            facecolor=color, edgecolor=edge, linewidth=lw,
        )
    else:
        patch = Rectangle((x, y), w, h, facecolor=color, edgecolor=edge, linewidth=lw)

    ax.add_patch(patch)
    if label:
        ax.text(x + w / 2, y + h / 2, str(value), ha="center", va="center",
                fontsize=13, color=readable(color))
    return color


def vis(counter, u):
    palette = shades(N)
    fig, ax = plt.subplots(figsize=(6, 6))
    for c in cells:
        x0, y0 = grid[c]
        v = solver.value(u[c])
        draw_rect(ax, x=x0, y=y0, value=v, n=N, palette=palette)

    ax.set_xlim(-0.2, N + 0.2)
    ax.set_ylim(-0.2, N + 0.2)
    ax.set_aspect("equal")

    for d, l in clues.items():
        if d == 'top':
            for i, cl in enumerate(l):
                plt.text(i + 0.5, N + 0.1, str(cl), fontweight="bold", ha="center", va="center", )
        if d == 'bottom':
            for i, cl in enumerate(l):
                plt.text(i + 0.5, -0.2, str(cl), fontweight="bold", ha="center", va="center", )
        if d == 'left':
            for i, cl in enumerate(l):
                plt.text(-0.2, N - i - 0.5, str(cl), fontweight="bold", ha="center", va="center", )
        if d == 'right':
            for i, cl in enumerate(l):
                plt.text(N + 0.2, N - i - 0.5, str(cl), fontweight="bold", ha="center", va="center", )

    ax.axis("off")
    plt.tight_layout()
    plt.savefig(f"rects {counter}.png", dpi=160, bbox_inches="tight")
    plt.show()


for c, u in collector.items():
    vis(c, u)
