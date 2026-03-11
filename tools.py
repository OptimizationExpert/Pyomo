import numpy as np

from base import Node


def make_data(puzzle_text):
    grid = puzzle_text.strip().split("\n")
    rows = len(grid)
    cols = len(grid[0])
    nodes = {}
    node_id = 1
    for r in range(rows + 1):
        for c in range(cols + 1):
            nodes[node_id] = (r, c)
            node_id += 1

    cells = {}
    cell_id = 1
    for r in range(rows):
        for c in range(cols):
            n1 = r * (cols + 1) + c + 1
            n2 = n1 + 1
            n3 = n1 + (cols + 1) + 1
            n4 = n1 + (cols + 1)

            char = grid[r][c]
            value = None if char == "." else int(char)

            cells[cell_id] = {
                "position": (r + 1, c + 1),
                "nodes": [n1, n2, n3, n4],  # TL, TR, BR, BL
                "value": value
            }

            cell_id += 1

    # -------------------------
    # Data dictionary
    # -------------------------
    data_dictionary = {
        "rows": rows,
        "cols": cols,
        "nodes": nodes,
        "cells": cells
    }
    return data_dictionary


def dist(i: Node, j: Node, node_by_id):
    x0, y0 = node_by_id[i].position
    x1, y1 = node_by_id[j].position
    return int(100 * (np.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)))


def neighbour(i: Node, j: Node):
    x0, y0 = i.position
    x1, y1 = j.position
    return int(abs(x0 - x1) + abs(y0 - y1)) == 1
