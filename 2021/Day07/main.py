file_path = "data.txt"

data = list(map(int, [f.strip('\n').split(',') for f in open(file_path)][0]))

data.sort()


def part1():
    median = data[int(len(data)/2)]
    fuel = 0
    for i in data:
        fuel += abs(median - i)
    return(fuel)


def part2():
    fuels = []
    for i in range(data[0], data[-1] + 1):
        fuel = 0
        for j in data:
            n = abs(j-i)
            fuel += int((n**2 + n) / 2)
        fuels.append(fuel)

    return(min(fuels))


print("Part1:", part1())
print("Part2:", part2())
