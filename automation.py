from ortools.sat.python import cp_model

# ---------------------------------------------------------
# پارامترهای مسئله
# ---------------------------------------------------------
num_nurses = 3
num_days = 14

# انواع شیفت
day_shift = 1
night_shift = 2
off_shift = 3
shifts = [day_shift, night_shift, off_shift]

model = cp_model.CpModel()

# ---------------------------------------------------------
# انتقال‌های اتوماتا (همان چیزی که فرستادی، دست‌نخورده)
# state 1 = تازه استراحت کرده / شروع
# state 2 = یک شیفت روز پشت‌سرهم کار کرده
# state 3 = یک شیفت شب پشت‌سرهم کار کرده
# state 4 = دو شیفت پشت‌سرهم کار کرده (فرقی نداره روز یا شب)
# state 6 = سه شیفت پشت‌سرهم کار کرده -> فقط مرخصی مجازه
# (state 5 در انتقال‌ها تعریف شده ولی هیچ یالی بهش نمی‌رسه؛ عملاً غیرقابل‌دسترسه)
# ---------------------------------------------------------
transitions = [
    (1, 3, 1),
    (1, 1, 2),
    (1, 2, 3),
    (2, 3, 1),
    (2, 1, 4),
    (2, 2, 4),
    (3, 1, 4),
    (3, 3, 1),
    (4, 1, 6),
    (4, 3, 1),
    (4, 2, 6),
    (5, 1, 6),
    (5, 3, 1),
    (6, 3, 1),
]

initial_state = 1
accepting_states = [1, 2, 3, 4]

# ---------------------------------------------------------
# متغیرهای تصمیم: شیفت هر پرستار در هر روز
# ---------------------------------------------------------
x = {}
for i in range(num_nurses):
    for j in range(num_days):
        x[i, j] = model.NewIntVar(min(shifts), max(shifts), 'x[%i,%i]' % (i, j))

# اعمال قید اتوماتا روی دنباله‌ی شیفت‌های هر پرستار
for i in range(num_nurses):
    y = [x[i, j] for j in range(num_days)]
    model.add_automaton(y, initial_state, accepting_states, transitions)

# ---------------------------------------------------------
# چند قید سبک اضافه، فقط تا جواب معنادار و غیر بدیهی بگیریم
# (اینها ربطی به AddAutomaton ندارند؛ صرفاً برای اجرا‌ی نمونه‌اند)
# ---------------------------------------------------------
is_day = {}
is_night = {}
for i in range(num_nurses):
    for j in range(num_days):
        is_day[i, j] = model.NewBoolVar(f"is_day_{i}_{j}")
        model.Add(x[i, j] == day_shift).OnlyEnforceIf(is_day[i, j])
        model.Add(x[i, j] != day_shift).OnlyEnforceIf(is_day[i, j].Not())

        is_night[i, j] = model.NewBoolVar(f"is_night_{i}_{j}")
        model.Add(x[i, j] == night_shift).OnlyEnforceIf(is_night[i, j])
        model.Add(x[i, j] != night_shift).OnlyEnforceIf(is_night[i, j].Not())

# هر روز حداقل یک پرستار در شیفت روز و یک پرستار در شیفت شب حضور داشته باشد
for j in range(num_days):
    model.Add(sum(is_day[i, j] for i in range(num_nurses)) >= 1)
    model.Add(sum(is_night[i, j] for i in range(num_nurses)) >= 1)

# ---------------------------------------------------------
# حل مدل
# ---------------------------------------------------------
solver = cp_model.CpSolver()
status = solver.Solve(model)

shift_name = {day_shift: "Day  ", night_shift: "Night", off_shift: "Off  "}
print("status:", solver.StatusName(status))

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    for i in range(num_nurses):
        row = " | ".join(str(solver.Value(x[i, j])) for j in range(num_days))
        print(f"Nurse {i + 1}: {row}")

