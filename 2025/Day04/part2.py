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


def find_removal_coords(grid):
    can_remove = []
    for idx_i, i in enumerate(grid):
        for idx_j, j in enumerate(i):
            if j == "@":
                if is_accessible(grid, idx_i, idx_j):
                    can_remove.append((idx_i, idx_j))
    return can_remove


def remove(grid, remove_coords):
    for i, j in remove_coords:
        grid[i][j] = "x"
    return grid


total_removed = 0

while True:
    remove_coords = find_removal_coords(grid)
    if len(remove_coords) == 0:
        break
    total_removed += len(remove_coords)
    grid = remove(grid, remove_coords)

print(total_removed)
