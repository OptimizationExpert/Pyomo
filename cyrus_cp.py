"""
================================================================================
 Title       : Cyrus the Great and the Halloween Curse - Haunted CVRP (CP-SAT)
 Description : Two-stage OR-Tools CP-SAT model for a capacitated vehicle routing
               problem with blocked roads.

 Cyrus the Great sends healing potions from Pasargadae (depot, node 0) to
 4 cities and 4 haunted settlements using 2 royal wagons (capacity 100 each).
 Four cursed roads cannot be used, so some locations can only be reached by
 passing through others.

 Stage 1 - Shortest paths: a network-flow model finds the minimum distance
           between every pair of nodes over the remaining roads, producing a
           complete distance matrix (e.g. 8 -> 1 = 8 -> 4 -> 0 -> 1 = 56 km).
 Stage 2 - CVRP: using that matrix, each location is served exactly once,
           both wagons start and end at Pasargadae, capacity is respected,
           and the total distance travelled is minimized.

 Long live Cyrus the Great, the man who wanted peace for humankind.

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Newsletter  : https://www.linkedin.com/pulse/cyrus-great-vs-halloween-curse-solving-haunted-vrp-soroudi-phd-ljenf
 Contact     : https://t.me/pypyid
 Udemy course (discount coupon): https://www.udemy.com/course/ortools-course/?couponCode=DISCOUNT_ORTOOLS
 Power System Optimization Course: https://optexpert.org/courses/advanced-power-system/
================================================================================
"""
import matplotlib.pyplot as plt
from ortools.sat.python import cp_model

from cyrus_data import *

solver = cp_model.CpSolver()

dist = {}
for (i,j,d) in safe_roads:
    dist[i,j] = d
    dist[j,i] = d

st,fn = 0 , 5

def short_path(st,fn):
    model = cp_model.CpModel()
    flow = {(i,j):model.new_bool_var(f"flow{i}_{j}") for (i,j) in dist.keys()}
    for n in nodes:
        if n==st:
            balance = 1
        elif n==fn:
            balance = -1
        else:
            balance = 0
        model.add(balance == sum(flow[n,j]-flow[j,n] for j in nodes if (n,j) in dist))

    of = [v*dist[i,j] for (i,j),v in flow.items()]
    model.minimize(sum(of))
    stat = solver.solve(model)
    return int(solver.objective_value)

add_dict = {}
for i in nodes:
    for j in nodes:
        if (i,j) not in dist and i!=j:
           add_dict[i,j] = short_path(i,j)
           add_dict[j,i] = add_dict[i,j]

global_dist = dist.copy()
global_dist.update(add_dict)
wagons = [w for w in range(number_of_vehicles)]

model = cp_model.CpModel()
flow = {(i, j,w): model.new_bool_var(f"flow{i}_{j}_{w}") for (i, j) in global_dist.keys()
        for w in wagons}
select = {(i,w): model.new_bool_var(f"assign{i}_{w}") for i in nodes
        for w in wagons}


for n in nodes:
    expr = [select[n,w] for w in wagons]
    if n != depot:
        model.add_exactly_one(expr)
    else:
        model.add(sum(expr) == number_of_vehicles)


for w in wagons:
    self_loop = [(n,n,v.Not()) for (n,ww),v in select.items() if n!=depot and w==ww]
    expr = [(i,j,v) for (i,j,ww),v in flow.items() if w==ww]
    model.add_circuit(self_loop+expr)

    total_load = sum([v*nodes[n]["demand"] for (n,ww),v in select.items() if w==ww])
    model.add(total_load <= vehicle_capacity)

of = [v * global_dist[i, j] for (i, j,w), v in flow.items()]
model.minimize(sum(of))
stat = solver.solve(model)
print(solver.status_name(stat), solver.objective_value)

colors = ['b','g']
for (i,j,w),v in flow.items():
    if solver.value(v)>0:
       x1,y1 = nodes[i]["x"],nodes[i]["y"]
       x2,y2 = nodes[j]["x"],nodes[j]["y"]
       plt.plot([x1,x2],[y1,y2],colors[w], zorder=2)
       plt.text(x1-0.2,y1-0.3,s=nodes[i]["name"],ha='center',va='center')
       plt.text(x2-0.2,y2-0.3,s=nodes[j]["name"],ha='center',va='center')
       plt.scatter(x1+0.1,y1+0.05,s=200, zorder= 5, c= 'gold')
       plt.text(x1,y1,s=str(i), zorder= 8)
       plt.scatter(x2+0.1,y2+0.05,s=200, zorder= 5, c= 'gold')
       plt.text(x2,y2,s=str(j), zorder= 8)
       xm,ym = 0.5*(x1+x2) , 0.5*(y1+y2)
       plt.text(xm, ym, s=str(global_dist[i,j]), zorder=8, fontsize= 8, fontweight= 'bold')

for (i,j) in dist.keys():
    x1, y1 = nodes[i]["x"], nodes[i]["y"]
    x2, y2 = nodes[j]["x"], nodes[j]["y"]
    plt.plot([x1, x2], [y1, y2], c='grey', lw= 7, alpha= 0.1, zorder= 1)


plt.grid(True)
plt.axis('off')
plt.tight_layout()
plt.show()









