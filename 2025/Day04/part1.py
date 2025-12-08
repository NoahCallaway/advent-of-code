file_path = "data.txt"

file = open(file_path).read().splitlines()

grid = [list(line) for line in file]


def is_accessible(grid, idx_i, idx_j):
    offsets = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    adjacent_rolls = 0
    for offset_i, offset_j in offsets:
        x = idx_i + offset_i
        y = idx_j + offset_j
        if x < 0 or x > len(grid) - 1 or y < 0 or y > len(grid[idx_i]) - 1:
            continue
        if grid[x][y] == "@":
            adjacent_rolls += 1
    return adjacent_rolls < 4


accesible_count = 0
for idx_i, i in enumerate(grid):
    for idx_j, j in enumerate(i):
        if j == "@":
            accesible_count += 1 if is_accessible(grid, idx_i, idx_j) else 0


print(accesible_count)
