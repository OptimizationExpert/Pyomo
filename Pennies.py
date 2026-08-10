import os

import matplotlib.pyplot as plt
import pyomo.environ as pyo
from matplotlib.patches import Circle
from pyomo import environ as pe
from pyomo.environ import *

os.environ['NEOS_EMAIL'] = 'x@gmail.com'
solver = pe.SolverManagerFactory('neos')

N = 16
r = 19.05 / 2
R = 4 * (2 * r) + 1.35 * r
print(R)
# R = 64.26
xmax, ymax = R - r, R - r

model = AbstractModel()
model.i = Set(initialize=RangeSet(N))
model.x = Var(model.i, bounds=(r, xmax), domain=pyo.Reals)
model.y = Var(model.i, bounds=(r, ymax), domain=pyo.Reals)


def rule_lim(model, i):
    return model.x[i] ** 2 + model.y[i] ** 2 <= (R - r) ** 2


model.lim1 = Constraint(model.i, rule=rule_lim)


def rule_lim2(model, i, j):
    if i > j:
        return (model.x[i] - model.x[j]) ** 2 + (model.y[i] - model.y[j]) ** 2 >= (2 * r) ** 2
    else:
        return Constraint.Skip


model.lim2 = Constraint(model.i, model.i, rule=rule_lim2)


def rule_obj(model):
    return sum(model.x[i] for i in model.i)


model.obj = Objective(rule=rule_obj, sense=maximize)
instance = model.create_instance()
results = solver.solve(instance, solver="ipopt")
print(f"OF = {round(value(instance.obj), 3)}")

plt.figure()
for i in instance.i:
    x0 = value(instance.x[i])
    y0 = value(instance.y[i])
    print(i, x0, y0)
    circle = Circle((x0, y0), r, fill=True)
    plt.gca().add_patch(circle)
    plt.text(x0, y0, f"{i}", zorder=3)

circle = Circle((0, 0), R, linewidth=2, fill=False)
plt.gca().add_patch(circle)

plt.xlim(0, R + 5)
plt.ylim(0, R + 5)
plt.tight_layout()
plt.grid()
plt.show()
