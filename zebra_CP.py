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
Houses = [f"h{i}" for i in range(1, 6)]
model = cp_model.CpModel()
x_color = {(h, color): model.new_bool_var(f"xcolor_{h}_{color}") for h in Houses for color in categories["colors"]}
x_nationality = {(h, n): model.new_bool_var(f"xnationality_{h}_{n}") for h in Houses for n in
                 categories["nationalities"]}
x_smoke = {(h, s): model.new_bool_var(f"xsmoke_{h}_{s}") for h in Houses for s in categories["cigarettes"]}
x_pets = {(h, p): model.new_bool_var(f"xpets_{h}_{p}") for h in Houses for p in categories["pets"]}
x_drink = {(h, d): model.new_bool_var(f"xdrink_{h}_{d}") for h in Houses for d in categories["drinks"]}

for h in Houses:
    expr_color = [x_color[h, color] for color in categories["colors"]]
    model.add_exactly_one(expr_color)

    expr_nationality = [x_nationality[h, n] for n in categories["nationalities"]]
    model.add_exactly_one(expr_nationality)

    expr_smoke = [x_smoke[h, s] for s in categories["cigarettes"]]
    model.add_exactly_one(expr_smoke)

    expr_pets = [x_pets[h, p] for p in categories["pets"]]
    model.add_exactly_one(expr_pets)

    expr_drink = [x_drink[h, d] for d in categories["drinks"]]
    model.add_exactly_one(expr_drink)


for c in categories["colors"]:
    model.add_exactly_one([x_color[h, c] for h in Houses])
for n in categories["nationalities"]:
    model.add_exactly_one([x_nationality[h, n] for h in Houses])
for p in categories["pets"]:
    model.add_exactly_one([x_pets[h, p] for h in Houses])
for d in categories["drinks"]:
    model.add_exactly_one([x_drink[h, d] for h in Houses])
for s in categories["cigarettes"]:
    model.add_exactly_one([x_smoke[h, s] for h in Houses])

for h in Houses:
    model.add(x_nationality[h, "Englishman"] == x_color[h, "Red"])
    model.add(x_nationality[h, "Spaniard"] == x_pets[h, "Dog"])
    model.add(x_drink[h, "Coffee"] == x_color[h, "Green"])
    model.add(x_nationality[h, "Ukrainian"] == x_drink[h, "Tea"])

    model.add(x_smoke[h, "Old Gold"] == x_pets[h, "Snails"])
    model.add(x_smoke[h, "Kools"] == x_color[h, "Yellow"])
    model.add(x_smoke[h, "Lucky Strike"] == x_drink[h, "Orange Juice"])
    model.add(x_smoke[h, "Parliaments"] == x_nationality[h, "Japanese"])
    h_index = Houses.index(h)
    xpcolor, xncolor = 0,0
    xphorse, xnhorse = 0,0
    xpfox, xnfox = 0,0
    if h_index + 1 < len(Houses):
        hp = Houses[h_index + 1]
        xpcolor = x_color[hp, 'Blue']
        xphorse = x_pets[hp, 'Horse']
        xpfox = x_pets[hp, 'Fox']
        model.add(x_color[hp, 'Green']==x_color[h, 'Ivory'])

    if h_index - 1 >= 0:
        hn = Houses[h_index - 1]
        x_color[hn, 'Blue']
        xncolor = x_color[hn, 'Blue']
        xnhorse = x_pets[hn, 'Horse']
        xnfox = x_pets[hn, 'Fox']

    model.add(x_color["h5", 'Ivory']==0)
    model.add(xpcolor+xncolor >= 1).only_enforce_if(x_nationality[h, "Norwegian"])
    model.add(xphorse+xnhorse >= 1).only_enforce_if(x_smoke[h, "Kools"])
    model.add(xpfox+xnfox >= 1).only_enforce_if(x_smoke[h, "Chesterfields"])

model.add(x_drink["h3", "Milk"] == True)
model.add(x_nationality["h1", "Norwegian"] == True)

solver = cp_model.CpSolver()
results = solver.Solve(model)
print(solver.status_name(results))


for h in Houses:
    KOLOR = [c for c in categories["colors"] if solver.Value(x_color[h, c])>0][0]
    national = [n for n in categories["nationalities"] if solver.Value(x_nationality[h, n])>0][0]
    smoke = [n for n in categories["cigarettes"] if solver.Value(x_smoke[h, n])>0][0]
    pet = [n for n in categories["pets"] if solver.Value(x_pets[h, n])>0][0]
    drink = [n for n in categories["drinks"] if solver.Value(x_drink[h, n])>0][0]

    print(f"{h}  {KOLOR} {national} {smoke} {pet} {drink}")
