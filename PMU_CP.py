"""
================================================================================
 Title       : Simple CP Model
 Description : This OR-Tools code solves the PMU allocation
 https://www.linkedin.com/pulse/cp-meets-power-grid-pmu-allocation-alireza-soroudi-phd-ewwmf/

A power system is observable when the voltage magnitude and angle are known at every bus.
A PMU measures the voltage at its own bus and the currents on its connected lines, so it observes that bus and all its neighbours.
PMU allocation finds the fewest buses to equip with PMUs so that every bus in the network is observed.

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
 Udemy course discount Coupon : https://www.udemy.com/course/ortools-course/?couponCode=DISCOUNT_ORTOOLS
 Power System Optimization Course: https://optexpert.org/courses/advanced-power-system/
================================================================================
"""
from ortools.sat.python import cp_model
from pmu_data import case_list
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import ListedColormap

solver = cp_model.CpSolver()
def opt_pmu(connect):
    connect = list({(i, j) if i < j else (j, i) for i, j in connect})
    buses = list({b for e in connect for b in e})
    model = cp_model.CpModel()
    install = {b: model.new_bool_var(f"install_{b}") for b in buses}

    adj = defaultdict(list)
    for i, j in connect:
        adj[i].append(j)
        adj[j].append(i)

    for b in buses:
        model.add_bool_or([install[b]] + [install[k] for k in adj[b]])

    of= [v for v in install.values()]
    model.minimize(cp_model.LinearExpr.Sum(of))
    status = solver.solve(model)
    toc = solver.user_time
    x={b:solver.value(v) for b,v in install.items()}
    boi = {b: x[b] + sum(x[k] for k in adj[b]) for b in buses}
    sori = round(sum(boi.values())/len(buses),3)  # system observability redundancy index
    single = sum(1 for b in buses if boi[b] == 1)  # buses lost if one PMU fails
    installed_busses=[b for b,v in install.items() if x[b]>0]

    print(solver.status_name(status), f"Buses {len(buses)} OF = ",solver.objective_value, f" sori {sori}, single {single}")
    return installed_busses, len(buses), single



def plot_placement(connect, pmus, title, fname=None, seed=7):
    G = nx.Graph()
    G.add_edges_from((i, j) for i, j in connect if i != j)
    pmu_set = set(pmus)
    boi = {b: (b in pmu_set) + sum(k in pmu_set for k in G[b]) for b in G}

    n = G.number_of_nodes()
    pos = nx.kamada_kawai_layout(G) if n <= 400 else nx.spring_layout(G, seed=seed, iterations=200)

    cmap = ListedColormap(["#d62728", "#ff7f0e", "#2ca02c", "#1f77b4"])  # BOI 1, 2, 3, 4+
    colors = [min(boi[b], 4) for b in G]

    fig, ax = plt.subplots(figsize=(16, 9), facecolor="white")
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color="#bbbbbb", width=0.8)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors, cmap=cmap, vmin=1, vmax=4,
                           node_size=60 if n > 100 else 220, linewidths=0)
    nx.draw_networkx_nodes(G, pos, nodelist=list(pmu_set), ax=ax, node_shape="s",
                           node_color="none", edgecolors="black", linewidths=1.6,
                           node_size=120 if n > 100 else 420)
    if n <= 60:
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=9)

    handles = [plt.Line2D([], [], marker="o", ls="", color=c, markersize=11, label=l)
               for c, l in zip(cmap.colors, ["BOI = 1", "BOI = 2", "BOI = 3", "BOI ≥ 4"])]
    handles.append(plt.Line2D([], [], marker="s", ls="", mfc="none", mec="black",
                              markersize=13, label="PMU"))
    ax.legend(handles=handles, loc="lower left", fontsize=14, frameon=False)
    ax.set_title(f"{len(pmus)} PMUs on {n} buses", fontsize=20)
    ax.axis("off")
    ax.margins(0.06)
    fig.tight_layout()
    if fname:
        fig.savefig(fname, dpi=200, facecolor="white")
    #plt.show().
    plt.close(fig)


X, Y, Z = [], [],[]
for case in case_list:
    pmus, nbus, s_outage = opt_pmu(case)
    X.append(nbus)
    Y.append(len(pmus)/nbus)
    Z.append(s_outage/nbus)

    if len(pmus)<0:
        plot_placement(case, pmus, str(case), f"pmu_{nbus}.png")

T= range(len(X))
plt.figure(figsize=[10, 5])
plt.scatter(T, Y, label="PMUs")
plt.scatter(T, Z, label="Single outage")
plt.xticks(T,X, rotation=90, fontsize=8, fontweight='bold')
plt.xlabel("Number of buses")
plt.ylabel("")
plt.grid(True)
plt.legend()
plt.savefig("all_pmus.png", dpi=200)
plt.show()