"""
================================================================================
 Title       : Simple CP Model
 Description : This OT-Tools code solves the a simple IP Problem

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""
import matplotlib
from ortools.sat.python import cp_model

matplotlib.use("Agg")  # non-interactive backend, safe to use from worker threads
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

KOLORS = ["#7f7f7f", "#bcbd22", "#17becf",
          "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5",
          "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
          "#8c6d31", "#9c9ede", "#637939", "#e7cb94", "#b5cf6b",
          "#cedb9c", "#c7c7c7", "#bd9e39", "#e7969c", "#7b4173"]
grid = {
    (1, 3): {"type": "clue", "value": 4, "shape": None},
    (1, 6): {"type": "filled", "value": None, "shape": "square"},
    (2, 2): {"type": "clue", "value": 3, "shape": None},
    (2, 7): {"type": "filled_clue", "value": 3, "shape": "tall_rectangle"},
    (3, 1): {"type": "clue", "value": 2, "shape": None},
    (3, 3): {"type": "clue", "value": 6, "shape": None},
    (3, 6): {"type": "filled", "value": None, "shape": "wide_rectangle"},
    (3, 8): {"type": "filled", "value": None, "shape": "tall_rectangle"},
    (6, 1): {"type": "filled", "value": None, "shape": "tall_rectangle"},
    (6, 3): {"type": "filled", "value": None, "shape": "wide_rectangle"},
    (6, 6): {"type": "clue", "value": 12, "shape": None},
    (6, 8): {"type": "clue", "value": 2, "shape": None},
    (7, 2): {"type": "filled_clue", "value": 5, "shape": "wide_rectangle"},
    (7, 7): {"type": "clue", "value": 3, "shape": None},
    (8, 3): {"type": "filled", "value": None, "shape": "wide_rectangle"},
    (8, 6): {"type": "clue", "value": 4, "shape": None},
}
N = 8

print(len(grid))

rects = {}
rects_by_rc = {}
i = 0
for (r, c), dic_data in grid.items():
    i += 1
    rects[i] = (r, c, dic_data)
    rects_by_rc[r, c] = i
cells = {}
counter = 0
for r in range(1, N + 1):
    for c in range(1, N + 1):
        counter += 1
        cells[counter] = (r, c)


def viz(counter, values, x_st, x_size, x_fn, y_st, y_size, y_fn):
    fig, ax = plt.subplots(figsize=(8, 8))

    for c in cells:
        (rr, cc) = cells[c]
        ax.text(cc - 0.5, N - rr + 1 - 0.5, s=str(c))

    for i in rects:
        (rr, cc, dic_data) = rects[i]
        x0, xl = values(x_st[i]), values(x_size[i])
        y0, yl = values(y_st[i]), values(y_size[i])
        ax.add_patch(
            Rectangle((x0, y0), xl, yl, linewidth=1, edgecolor='k', facecolor=KOLORS[i - 1], alpha=1))
        xr, yr = cc - 0.5, N - rr + 1 - 0.5
        #ax.text(xr - 0.2, yr - 0.2, s=str(i))
        #ax.scatter(xr, yr, s=100, c='k', zorder=2)

    ax.set_xlim(0, N)
    ax.set_ylim(0, N)
    ax.set_aspect('equal')
    ax.set_xticks(range(N + 1))
    ax.set_yticks(range(N + 1))
    ax.grid(True, linewidth=0.5, alpha=0.5)

    fig.savefig(f"figure {counter}.png")
    plt.close(fig)

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, xst, xsize, xfn, yst, ysize, yfn):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__xst = xst
        self.__xsize = xsize
        self.__xfn = xfn
        self.__yst = yst
        self.__ysize = ysize
        self.__yfn = yfn
        self.__solution_count = 0

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        print(f"Solution {self.__solution_count}")
        viz(self.__solution_count, self.value, self.__xst, self.__xsize, self.__xfn,
            self.__yst, self.__ysize, self.__yfn)
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count

model = cp_model.CpModel()

u = {c: model.new_bool_var(f"u_{c}") for c in cells}
x = {(c, i): model.new_bool_var(f"x_{c}_{i}") for c in cells
     for i in rects}
x_st = {i: model.new_int_var(0, N-1, f"xst_{i}") for i in rects}
x_size = {i: model.new_int_var(1, N, f"xsize_{i}") for i in rects}
x_fn = {i: model.new_int_var(1, N, f"xfn_{i}") for i in rects}

y_st = {i: model.new_int_var(0, N-1, f"yst_{i}") for i in rects}
y_size = {i: model.new_int_var(1, N, f"ysize_{i}") for i in rects}
y_fn = {i: model.new_int_var(1, N, f"yfn_{i}") for i in rects}

xintervals = {i: model.new_interval_var(x_st[i], x_size[i], x_fn[i], f"xint_{i}")
              for i in rects}
yintervals = {i: model.new_interval_var(y_st[i], y_size[i], y_fn[i], f"yint_{i}")
              for i in rects}

xintervals_list = [xint for i, xint in xintervals.items()]
yintervals_list = [yint for i, yint in yintervals.items()]

for c in cells:
    if cells[c] in grid:
        i = rects_by_rc[cells[c]]
        model.add(x[c, i] == 1)
    else:
        expr = [x[c, i] for i in rects]
        model.add_exactly_one(expr)
for i in rects:
    (rr, cc, dic_data) = rects[i]
    if dic_data["value"]:
        expr = [x[c, i] for c in cells]
        model.add(sum(expr) == dic_data["value"])
    for c in cells:
        (rr, cc) = cells[c]
        xm,ym = cc,N-rr+1
        print((rr,cc),'-------->',(xm,ym))
        model.add(ym <= y_fn[i]).only_enforce_if(x[c, i])
        model.add(ym-1 >= y_st[i]).only_enforce_if(x[c, i])
        model.add(xm <= x_fn[i]).only_enforce_if(x[c, i])
        model.add(xm-1 >= x_st[i]).only_enforce_if(x[c, i])

    if dic_data["shape"] == "tall_rectangle":
       model.add(y_size[i]>x_size[i])
       print('TAG1',i,dic_data["value"])
    elif dic_data["shape"] == "wide_rectangle":
       model.add(y_size[i]<x_size[i])
       print('TAG2',i,dic_data["value"])

    elif dic_data["shape"] == "square":
       model.add(y_size[i]==x_size[i])



model.add_no_overlap_2d(xintervals_list, yintervals_list)

solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter(x_st,x_size,x_fn,y_st,y_size,y_fn)

results = solver.Solve(model,solution_printer)
print(solver.status_name(results))

