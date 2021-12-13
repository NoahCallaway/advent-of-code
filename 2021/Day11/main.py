file_path = "data.txt"

grid = [list(map(int, list(line)))
        for line in open(file_path).read().splitlines()]


def increment(grid):
    # increase all by one
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1
    return flashes(grid)


def flashes(grid):
    flashed = []
    did_flash = True
    width = len(grid[0])
    height = len(grid)

    def _handle_adjacent(i, j):
        ords = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                (1, 1), (1, 0), (1, -1), (0, -1)]
        for dy, dx in ords:
            x = i + dx
            y = j + dy
            if 0 <= x < width and 0 <= y < height:
                grid[x][y] = grid[x][y] + \
                    1 if (x, y) not in flashed else grid[x][y]

    while did_flash:
        did_flash = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 9:
                    did_flash = True
                    grid[i][j] = 0
                    if (i, j) not in flashed:
                        flashed.append((i, j))
                        _handle_adjacent(i, j)

    return grid, len(flashed)


def is_sync(grid):
    for line in grid:
        if line != grid[0]:
            return False
    return True


def part1(grid):
    total_flash = 0
    for i in range(100):
        grid, flash = increment(grid)
        total_flash += flash
    print("Part 1:", total_flash)


def part2(grid):
    step = 100
    sync = False
    while not sync:
        step += 1
        grid, flash = increment(grid)
        sync = is_sync(grid)
    print("Part 2:", step)


part1(grid)
part2(grid)
