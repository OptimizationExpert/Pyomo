"""
Developed by Alireza Soroudi
alireza.soroudi@gmail.com
optexpert.org

"""
from ortools.sat.python import cp_model # CP-SAT solver
import matplotlib.pyplot as plt

def min_ops_sequence(target):
    max_steps = 50

    model = cp_model.CpModel()
    steps = list(range(1, max_steps + 1))

    U = {s: model.new_bool_var(f"continue_{s}") for s in steps}
    P = {s: model.new_bool_var(f"plus_{s}") for s in steps}
    Z = {s: model.new_bool_var(f"multiply_{s}") for s in steps}
    disp = {s: model.new_int_var(min(s, target), target, f"disp_{s}") for s in steps}

    for s in steps:
        model.add(P[s] + Z[s] == U[s])
        if s == 1:
            model.add(disp[s] == 1)
        else:
            model.add(disp[s] == disp[s - 1] + 1).only_enforce_if(P[s])
            model.add(disp[s] == 10 * disp[s - 1]).only_enforce_if(Z[s])
            model.add(disp[s] == disp[s - 1]).only_enforce_if(U[s].Not())
            model.add(disp[s] >= disp[s - 1])
        if s + 1 in steps and s > 1:
            model.add(disp[s] == target).only_enforce_if(U[s + 1].Not())

    model.add(disp[max_steps] == target)
    model.minimize(sum(s * U[s] for s in steps))

    solver = cp_model.CpSolver()
    status = solver.solve(model)
    print(solver.status_name(status))
    ops = []
    for s in steps:
        if solver.value(U[s]) == 0:
            continue
        ops.append("+1" if solver.value(P[s]) == 1 else "x10")
        if solver.value(disp[s]) == target:
            break
    return ops


def trajectory(target):
    ops = min_ops_sequence(target)
    values = [1]
    for op in ops:
        values.append(values[-1] + 1 if op == "+1" else values[-1] * 10)
    return values, ops


def plot_sequence(target, ax):
    values, ops = trajectory(target)
    steps = list(range(len(values)))
    ax.plot(steps, values, color="#9AA7B3", linewidth=1, zorder=1)

    plus_steps = [i for i in steps[1:] if ops[i - 1] == "+1"]
    plus_vals = [values[i] for i in plus_steps]
    mul_steps = [i for i in steps[1:] if ops[i - 1] == "x10"]
    mul_vals = [values[i] for i in mul_steps]

    ax.scatter(plus_steps, plus_vals, color="#2563EB", marker="o", s=35, zorder=2, label="+1")
    ax.scatter(mul_steps, mul_vals, color="#D97706", marker="^", s=55, zorder=2, label="x10")
    ax.scatter([0], [1], color="#6B7280", marker="s", s=40, zorder=2, label="start")

    ax.set_yscale("log")
    ax.set_title(f"target = {target}  ({len(ops)} keys)", fontsize=11)
    ax.set_xlabel("step")
    ax.set_ylabel("display value")
    ax.grid(True, which="both", linewidth=0.3, alpha=0.5)
    ax.legend(fontsize=8, loc="lower right")


def plot_many(targets):
    n = len(targets)
    cols = 3
    rows = -(-n // cols)  # ceil
    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 4 * rows))
    axes = axes.flatten() if n > 1 else [axes]

    for ax, target in zip(axes, targets):
        plot_sequence(target, ax)

    for ax in axes[n:]:
        ax.axis("off")

    fig.tight_layout()
    fig.savefig("calculator_sequences.png", dpi=150)
    plt.show()


if __name__ == "__main__":
  def primes_between(a, b):
    return [n for n in range(a, b + 1) if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))]
  plot_many(primes_between(900, 1000))