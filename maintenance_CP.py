"""
================================================================================
 Title       : <Tiling Puzzle>
 Description : This OT-Tools code solves the tiling puzzle

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""
from matplotlib import pyplot as plt
from ortools.sat.python import cp_model
from data_maintenance_CP import jobs, job_machine_order, op_du, machines, maintenance

solver = cp_model.CpSolver()
model = cp_model.CpModel()

tmax = int(24 * 4 + 22) - 6
start = {(j, m): model.new_int_var(0, tmax - op_du[j, m], f"start{j}-{m}")
         for (j, m) in op_du.keys()
         }
late = {j: model.new_int_var(0, 48, f"late{j}")
        for j in jobs
        }

jm_interval = {(j, m): model.new_fixed_size_interval_var(start[j, m], op_du[j, m], f"start_interval{j}-{m}")
               for (j, m), v in start.items()
               }

maintenance_start = {m: model.new_int_var(maintenance[m]["fr"], maintenance[m]["to"] - maintenance[m]["du"], f"st _{m}")
                     for m in maintenance}
maintenance_interval = {
    m: model.new_fixed_size_interval_var(maintenance_start[m], maintenance[m]["du"], f"intervals st _{m}")
    for m in maintenance}

for j in jobs:
    for m in machines:
        for m2 in machines:
            if (j, m) in op_du and (j, m2) in op_du and job_machine_order.index((j, m)) < job_machine_order.index(
                    (j, m2)):
                model.add(start[j, m] + op_du[j, m] <= start[j, m2])
for m in machines:
    expr_intervals = [jm_interval[j, m] for j in jobs if (j, m) in jm_interval]
    expr_intervals+=[maintenance_interval[m]]

    model.add_no_overlap(expr_intervals)

for j, v_late in late.items():
    for m in machines:
        if (j, m) in start:
            model.add(v_late >= start[j, m] + op_du[j, m] - jobs[j]["due"])

no_overlap_maintenance = [v for m, v in maintenance_interval.items()]
model.add_no_overlap(no_overlap_maintenance)

of = [v_late * jobs[j]["weight"] for j, v_late in late.items()]
model.minimize(sum(of))

status = solver.Solve(model)
print(solver.status_name(status), solver.objective_value)
KOLORs = ['r', 'b', 'gold', 'g', 'k', 'brown']
jobnames = [j for j in jobs]
fn_vec = []

for j, v_late in late.items():
    if solver.value(v_late) > 0:
        print(j, jobs[j]['weight'], solver.value(v_late))
for (j, m), v in start.items():
    st = solver.value(v)
    fn = st + op_du[j, m]
    y = jobnames.index(j)
    kindex = machines.index(m)
    plt.plot([st, fn], [y, y], c=KOLORs[kindex], lw=3)

    plt.scatter(jobs[j]["due"], y, s=100, c='k', marker='|')
    fn_vec.append(fn)

for m, v_st_maintenance in maintenance_start.items():
    st = solver.value(v_st_maintenance)
    fn = st + maintenance[m]["du"]
    print(m, st, fn)
    y = len(jobnames) + 1
    kindex = machines.index(m)
    plt.plot([st, fn], [y, y], c=KOLORs[kindex], lw=3, alpha=0.6, label=f"{m}")
plt.yticks(range(len(jobs)), jobnames)
print('max fn', max(fn_vec))
plt.xticks(range(0, max(fn_vec) + 6, 6), fontweight='bold', rotation='vertical')
plt.yticks(fontweight='bold')
plt.grid(alpha=0.5)
plt.legend()
plt.xlabel("Time")
plt.ylabel("Jobs")
plt.tight_layout()
plt.show()
