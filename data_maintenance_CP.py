jobs = {
    "J1": {"product": "Drive shaft", "due": 96, "due_time": "Fri 06:00", "priority": "Medium", "weight": 2},
    "J2": {"product": "Pump flange", "due": 80, "due_time": "Thu 14:00", "priority": "Low", "weight": 1},
    "J3": {"product": "Gearbox housing", "due": 110, "due_time": "Fri 20:00", "priority": "Low", "weight": 1},
    "J4": {"product": "Spindle (rush)", "due": 72, "due_time": "Thu 06:00", "priority": "High", "weight": 3},
    "J5": {"product": "Valve flange", "due": 100, "due_time": "Fri 10:00", "priority": "Medium", "weight": 2},
    "J6": {"product": "Bearing housing", "due": 104, "due_time": "Fri 14:00", "priority": "Medium", "weight": 2},
}

routes = {
    "J1": [("Lathe", 24), ("Drill", 8), ("Furnace", 16), ("Grinder", 16)],
    "J2": [("Lathe", 12), ("Drill", 12), ("Milling", 16)],
    "J3": [("Milling", 20), ("Furnace", 12), ("Drill", 8)],
    "J4": [("Lathe", 20), ("Milling", 8), ("Furnace", 16), ("Grinder", 20)],
    "J5": [("Lathe", 12), ("Drill", 8), ("Milling", 12), ("Grinder", 8)],
    "J6": [("Milling", 24), ("Lathe", 16), ("Drill", 12)],
}

maintenance = {
    "Lathe": {"du": 8, "fr": 24, "to": 48},
    "Milling": {"du": 8, "fr": 16, "to": 40},
    "Drill": {"du": 4, "fr": 48, "to": 64},
    "Furnace": {"du": 12, "fr": 30, "to": 60},
    "Grinder": {"du": 6, "fr": 60, "to": 84},
}

job_machine_order = [(j, m) for j in routes for (m, du) in routes[j]]
op_du = {(j, m): du for j in routes for (m, du) in routes[j]}
machines = list({m for ops in routes.values() for (m, du) in ops})
