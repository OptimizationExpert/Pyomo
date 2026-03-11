from dataclasses import dataclass
from typing import Tuple, List, Optional


@dataclass
class Node:
    name: int
    position: Tuple[int, int]  # (row, col)

    def __hash__(self):
        return hash(self.name)


Nodes = List[Node]


@dataclass
class Cell:
    name: int
    position: Tuple[int, int]  # (row, col)
    nodes: Nodes  # [top_left, top_right, bottom_right, bottom_left]
    value: Optional[int]  # clue value or None

    def __hash__(self):
        return hash(self.name)


Cells = List[Cell]
