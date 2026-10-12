"""
Data
https://github.com/MiniZinc/mzn-challenge/blob/develop/2012/amaze/2012-03-15.dzn

 Description : This OT-Tools code solves the PCB Problem
 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""


from ortools.sat.python import cp_model
import matplotlib.pyplot as plt



X = 10
Y = 10
N = 7
end_points_start_x = [2, 4, 2, 2, 4, 3, 1]
end_points_start_y = [6, 6, 7, 3, 8, 2, 1]
end_points_end_x = [5, 8, 5, 3, 9, 8, 7]
end_points_end_y = [3, 8, 8, 8, 2, 7, 5]


X = 12
Y = 15
N = 16
end_points_start_x = [6, 4, 2, 1, 11, 3, 6, 3, 7, 2, 1, 4, 3, 6, 1, 11]
end_points_start_y = [10, 15, 7, 15, 13, 9, 14, 14, 1, 11, 1, 3, 2, 4, 5, 8]
end_points_end_x = [10, 11, 11, 11, 12, 7, 12, 6, 9, 3, 10, 6, 7, 8, 5, 12]
end_points_end_y = [8, 12, 7, 6, 15, 11, 14, 11, 10, 15, 4, 1, 4, 5, 5, 13]


data = {}
counter = 0
node_by_cord = {}
for x in range(1,1+X):
    for y in range(1,1+Y):
        counter += 1
        data[counter]=(x,y)
        node_by_cord[x,y] = counter
        print(x,y)


pairs = []
groups = [g for g in range(N)]

for n in groups:
    st_cord = (end_points_start_x[n],end_points_start_y[n])
    st = node_by_cord[st_cord]
    fn_cord = (end_points_end_x[n],end_points_end_y[n])
    fn = node_by_cord[fn_cord]
    pairs.append((st,fn))

print(pairs)


def dist(n1,n2):
    if abs(data[n1][0]- data[n2][0])+abs(data[n1][1]- data[n2][1]) ==1:
       return True
    else:
       return False
model = cp_model.CpModel()
solver = cp_model.CpSolver()
nodes = [n for n in range(1,1+counter)]

select = {(node,g):model.new_bool_var(f"{node}_{g}") for node in nodes for g in groups}
x= {(n1,n2,g):model.new_bool_var(f"{n1}_{n2}_{g}") for n1 in nodes for n2 in nodes for g in groups
    if n1!=n2 and dist(n1,n2)}


for g in groups:
    (st,fn) = pairs[g]
    model.add(select[st,g] == 1)
    model.add(select[fn,g] == 1)
    for gg in groups:
        if g!= gg:
          model.add(select[st,gg] == 0)
          model.add(select[fn,gg] == 0)

    self_loop = [(n1,n1,v.Not()) for (n1,gg),v in select.items() if gg==g]
    return_path = [(fn,st,True)]
    expr_loop = [(n1,n2,v) for (n1,n2,gg),v in x.items() if gg==g] +self_loop + return_path
    model.add_circuit(expr_loop)

for (n1,n2,g),v in x.items():
    model.add(v<= select[n1,g])
    model.add(v<= select[n2,g])

for n in nodes:
    expr = [select[n,g] for g in groups]
    model.add_exactly_one(expr)


status = solver.Solve(model)
print(solver.status_name(status))

colors = [
    "tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple",
    "tab:brown", "tab:pink", "tab:gray", "tab:olive", "tab:cyan",
    "navy", "gold", "lime", "crimson", "teal",
    "darkorange", "magenta", "saddlebrown", "slateblue", "black",
]


plt.figure()
for n, (x0,y0) in data.items():
    plt.scatter(x0,Y-y0, s= 550 , marker = 's', alpha = 0.5, c='grey')
    for g in groups:
        (st, fn) = pairs[g]
        x1,y1 = data[st]
        plt.scatter(x1, Y - y1, s=550, marker='s', alpha=0.5, c=colors[g])
        x2,y2 = data[fn]
        plt.scatter(x2, Y - y2, s=550, marker='s', alpha=0.5, c=colors[g])

plt.tight_layout()
plt.axis('off')
plt.savefig('base PCB.png')
for (n,g),v in select.items():
    if solver.value(v)>0:
       x0,y0 = data[n]
       plt.scatter(x0, Y - y0, s=550, marker='s', alpha=0.2, c=colors[g])

for (n1,n2,g),v in x.items():
    if solver.value(v)>0:
       x1,y1 = data[n1]
       x2,y2 = data[n2]
       plt.plot([x1,x2], [Y-y1,Y-y2], '-', color = colors[g], lw= 4, alpha = 0.2,zorder=-2)


plt.tight_layout()
plt.savefig('path PCB.png')
plt.show()










