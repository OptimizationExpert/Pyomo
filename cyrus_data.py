# ============================================================
# CYRUS THE GREAT — HALLOWEEN HEALTHCARE VRP
# ============================================================

# 1. LOCATIONS
# Coordinates: (x, y) for graphical visualization
# Demand: Number of healing potions required

nodes = {
    0: {"name": "Pasargadae",     "type": "depot",   "x": 5,  "y": 3, "demand": 0},
    1: {"name": "Persepolis",     "type": "city",    "x": 8,  "y": 1, "demand": 25},
    2: {"name": "Susa",           "type": "city",    "x": 1,  "y": 4, "demand": 30},
    3: {"name": "Ecbatana",       "type": "city",    "x": 6,  "y": 8, "demand": 20},
    4: {"name": "Babylon",        "type": "city",    "x": 8,  "y": 4, "demand": 35},
    5: {"name": "Haunted Temple", "type": "haunted", "x": 1,  "y": 8, "demand": 10},
    6: {"name": "Ghost Valley",   "type": "haunted", "x": 1,  "y": 1, "demand": 15},
    7: {"name": "Witch Forest",   "type": "haunted", "x": 10, "y": 8, "demand": 20},
    8: {"name": "Pumpkin Castle", "type": "haunted", "x": 11, "y": 4, "demand": 15},
}

# 2. VEHICLES
vehicles = {
    0: {"name": "Royal Wagon A", "capacity": 100, "start": 0, "end": 0},
    1: {"name": "Royal Wagon B", "capacity": 100, "start": 0, "end": 0},
}

# 3. ROAD NETWORK
# Format: (node_i, node_j, distance)
# All roads are bidirectional.
# Distances are fictional kilometres.

roads = [
    (0, 1, 12),
    (0, 2, 28),
    (0, 3, 20),
    (0, 4, 30),
    (0, 5, 22),
    (0, 6, 14),

    (1, 4, 20),
    (1, 8, 25),

    (2, 3, 22),
    (2, 5, 18),
    (2, 6, 12),

    (3, 4, 18),
    (3, 5, 25),
    (3, 7, 11),

    (4, 7, 20),
    (4, 8, 14),

    (7, 8, 16),
]

# 4. CURSED ROADS
# Roads blocked by Halloween creatures
# These roads cannot be used by medical wagons.

cursed_roads = [
    (1, 4),  # Persepolis - Babylon
    (1, 8),  # Persepolis - Pumpkin Castle
    (2, 3),  # Susa - Ecbatana
    (4, 7),  # Babylon - Witch Forest
]

# 5. PUZZLE PARAMETERS

depot = 0
number_of_vehicles = len(vehicles)
vehicle_capacity = 100
customers = [i for i in nodes if i != depot]
total_demand = sum(nodes[i]["demand"] for i in customers)
total_capacity = sum(v["capacity"] for v in vehicles.values())
# 6. SAFE ROAD NETWORK

blocked = {tuple(sorted(edge)) for edge in cursed_roads}

safe_roads = [
    (i, j, d)
    for i, j, d in roads
    if tuple(sorted((i, j))) not in blocked
]

# 7. SUMMARY
