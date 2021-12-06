import copy

file_path = "data.txt"
data = open(file_path).read().splitlines()

coords = []
for line in data:
    line = line.split(' -> ')
    for i, ord in enumerate(line):
        line[i] = tuple(map(int, ord.split(',')))
    coords.append(line)


def is_vertical(ord_pair):
    return True if ord_pair[0][0] == ord_pair[1][0] else False


def is_horizontal(ord_pair):
    return True if ord_pair[0][1] == ord_pair[1][1] else False


def draw_line(ord_pair, grid):
    x1 = ord_pair[0][0]
    x2 = ord_pair[1][0]
    y1 = ord_pair[0][1]
    y2 = ord_pair[1][1]

    if is_horizontal(ord_pair):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1

    elif is_vertical(ord_pair):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1

    else:
        x_inc = -1 if x2 - x1 < 0 else 1
        y_inc = -1 if y2 - y1 < 0 else 1

        x_ords = [x for x in range(x1, x2 + x_inc, x_inc)]
        y_ords = [y for y in range(y1, y2 + y_inc, y_inc)]

        for i in range(len(y_ords)):
            grid[y_ords[i]][x_ords[i]] += 1

    return(grid)


def count_overlap(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 1:
                count += 1
    return(count)


def part1(grid):
    for ord_pair in coords:
        if is_vertical(ord_pair) or is_horizontal(ord_pair):
            grid = draw_line(ord_pair, grid)

    print("Part 1:", count_overlap(grid))


def part2(grid):
    for ord_pair in coords:
        grid = draw_line(ord_pair, grid)
    print("Part 2:", count_overlap(grid))


largest = max(max(max(j) for j in i) for i in coords) + 1
ocean_floor = [[0 for i in range(largest)] for j in range(largest)]

part1(copy.deepcopy(ocean_floor))
part2(copy.deepcopy(ocean_floor))
