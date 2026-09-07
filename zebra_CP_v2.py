"""
================================================================================
 Title       : Simple CP Model
 Description : This OT-Tools code solves the Zebra Puzzle
 https://dmcommunity.org/challenges/2026-09-zebra-puzzle/

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
================================================================================
"""
from ortools.sat.python import cp_model

categories = {
    "colors": ["Yellow", "Blue", "Red", "Ivory", "Green"],
    "nationalities": ["Norwegian", "Ukrainian", "Englishman", "Spaniard", "Japanese"],
    "drinks": ["Water", "Tea", "Milk", "Orange Juice", "Coffee"],
    "cigarettes": ["Kools", "Chesterfields", "Old Gold", "Lucky Strike", "Parliaments"],
    "pets": ["Fox", "Horse", "Snails", "Dog", "Zebra"],
}
Houses = [i for i in range(1, 6)]
model = cp_model.CpModel()
x_assign = {(category, element): model.new_int_var(1, 5, f"assign_{category}_{element}") for category, elements in
            categories.items() for element in elements}

for category, elements in categories.items():
    expr = [x_assign[category, e] for e in elements]
    model.add_all_different(expr)

model.add(x_assign["nationalities", "Englishman"] == x_assign["colors", "Red"])
model.add(x_assign["nationalities", "Spaniard"] == x_assign["pets", "Dog"])
model.add(x_assign["drinks", "Coffee"] == x_assign["colors", "Green"])
model.add(x_assign["drinks", "Tea"] == x_assign["nationalities", "Ukrainian"])
model.add(x_assign["cigarettes", "Old Gold"] == x_assign["pets", "Snails"])
model.add(x_assign["cigarettes", "Kools"] == x_assign["colors", "Yellow"])
model.add(x_assign["drinks", "Orange Juice"] == x_assign["cigarettes", "Lucky Strike"])
model.add(x_assign["nationalities", "Japanese"] == x_assign["cigarettes", "Parliaments"])
model.add(x_assign["colors", "Green"] == 1 + x_assign["colors", "Ivory"])
model.add(x_assign["drinks", "Milk"] == 3)
model.add(x_assign["nationalities", "Norwegian"] == 1)
model.add(x_assign["cigarettes", "Chesterfields"] - x_assign["pets", "Fox"] <= 1)
model.add(x_assign["cigarettes", "Chesterfields"] - x_assign["pets", "Fox"] >= -1)
model.add_all_different(x_assign["cigarettes", "Chesterfields"], x_assign["pets", "Fox"])

model.add(x_assign["cigarettes", "Kools"] - x_assign["pets", "Horse"] <= 1)
model.add(x_assign["cigarettes", "Kools"] - x_assign["pets", "Horse"] >= -1)
model.add_all_different(x_assign["cigarettes", "Kools"], x_assign["pets", "Horse"])

model.add(x_assign["nationalities", "Norwegian"] - x_assign["colors", "Blue"] <= 1)
model.add(x_assign["nationalities", "Norwegian"] - x_assign["colors", "Blue"] >= -1)
model.add_all_different(x_assign["nationalities", "Norwegian"], x_assign["colors", "Blue"])

solver = cp_model.CpSolver()
results = solver.Solve(model)
print(solver.status_name(results))

for h in Houses:
    KOLOR = [c for c in categories["colors"] if solver.Value(x_assign['colors', c]) == h][0]

    national = [n for n in categories["nationalities"] if solver.Value(x_assign["nationalities", n]) == h][0]
    smoke = [n for n in categories["cigarettes"] if solver.Value(x_assign["cigarettes", n]) == h][0]
    pet = [n for n in categories["pets"] if solver.Value(x_assign["pets", n]) == h][0]
    drink = [n for n in categories["drinks"] if solver.Value(x_assign["drinks", n]) == h][0]

    print(f"House {h} {pet}--> {KOLOR} {national} {smoke}  {drink}")
