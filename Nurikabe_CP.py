"""
================================================================================
 Title       : Simple CP Model
 Description : This OT-Tools code solves the Zebra Puzzle
 https://dmcommunity.org/challenges/2026-09-zebra-puzzle/

 Developed by: Dr. Alireza Soroudi
 Website     : https://optexpert.org/
 Contact     : https://t.me/pypyid
 udemy courses :
 ORTools --> https://www.udemy.com/course/ortools-course/?couponCode=DISCOUNT_ORTOOLS
 Pyomo --->
 GAMS in Power Systems -->
================================================================================
"""
from ortools.sat.python import cp_model
solver = cp_model.CpSolver()
grid = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

nr,nc = len(grid), len(grid[0])
cells, data = {} , {}
n = 0
all_islands = {}
island_number = 0
for r in range(nr):
    for c in range(nc):
        n+=1
        cells[n] = [r, c,grid[r][c]]
        data[r,c] = n
        if grid[r][c]>0:
            island_number+=1
            all_islands[island_number] = (n,grid[r][c])

islands = [i for i in range(1,len(all_islands)+1)]
all_area = [0]+islands
nodes = [n for n in cells]
model = cp_model.CpModel()
assign = {(n,area): model.new_bool_var(f"assign_{n}_{area}") for n in nodes for area in all_area}

for n in nodes:
    for area in islands:
        if all_islands[area][0] == n:
            model.add(assign[n,area]==1)



for n in nodes:
    expr = [assign[n,area] for area in all_area]
    model.add_exactly_one(expr)
stat = solver.Solve(model)
print(solver.status_name(stat))


