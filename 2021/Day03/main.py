file_path = "data.txt"

data = open(file_path).read().splitlines()


def binary_to_decimal(binary):
    return int("".join(str(i) for i in binary), 2)


def keep_lines_with(char: str, pos: int,  lines: list):
    new_list = []
    for line in lines:
        if line[pos] == char:
            new_list.append(line)
    return(new_list)


def one_most_common(pos: int, lines: list):
    count_ones = 0
    for line in lines:
        if line[pos] == '1':
            count_ones += 1

    if count_ones > len(lines) / 2 or count_ones == len(lines) / 2:
        return True
    else:
        return False


def calc_oxygen(data: list, pos: int):
    if len(data) > 1:
        char = '1' if one_most_common(pos, data) else '0'
        return calc_oxygen(keep_lines_with(char, pos, data), pos + 1)
    else:
        return int(data[0], 2)


def calc_CO2(data: list, pos: int):
    if len(data) > 1:
        char = '0' if one_most_common(pos, data) else '1'
        return calc_CO2(keep_lines_with(char, pos, data), pos + 1)
    else:
        return int(data[0], 2)


def part1():
    gamma_rate = [0] * len(data[0])
    epsilon_rate = [1] * len(data[0])

    for i in range(len(data[0])):
        if one_most_common(i, data):
            gamma_rate[i] = 1
            epsilon_rate[i] = 0

    return binary_to_decimal(gamma_rate) * binary_to_decimal(epsilon_rate)


def part2():
    return calc_oxygen(data, 0) * calc_CO2(data, 0)


print("Part 1:", part1())
print("Part 2:", part2())
