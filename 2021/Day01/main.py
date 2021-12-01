task_file = "data.txt"

lines = list(map(int, open(task_file).read().splitlines()))


def part1():
    count_increase = 0

    for i, line in enumerate(lines):
        if i == 0:
            continue
        if line > lines[i-1]:
            count_increase += 1

    return count_increase


def part2():
    sum_list = []
    count_increase = 0

    for i, line in enumerate(lines):
        if i >= 2:
            sum_list.append(sum(lines[i-3:i]))

            if len(sum_list) > 1 and sum_list[-1] > sum_list[-2]:
                count_increase += 1

    return count_increase


print("Part 1:", part1())
print("Part 2:", part2())
