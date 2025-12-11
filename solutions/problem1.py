# combined_solution.py
# SOSC Round 2 — compute Clue1, Clue2, Clue3 and final key

from math import isqrt

# -------------------------------
# Problem 1 — Grid Rotation
# -------------------------------
with open("inputs/grid.txt") as f:
    grid = [line.strip() for line in f.readlines()]

with open("inputs/directions.txt") as f:
    directions = f.read().strip().split()

if len(grid) != len(directions):
    raise ValueError("Number of directions does not match number of rows in the grid")

rotated_grid = []
for row, dir in zip(grid, directions):
    if dir.upper() == "R":
        rotated_row = row[-1] + row[:-1]
    elif dir.upper() == "L":
        rotated_row = row[1:] + row[0]
    else:
        raise ValueError(f"Invalid direction: {dir}")
    rotated_grid.append(rotated_row)

mid_index = len(rotated_grid) // 2
middle_row = rotated_grid[mid_index]
clue1 = sum(ord(c) for c in middle_row)
print("Clue1 (decimal):", clue1)
