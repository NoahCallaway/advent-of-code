file_path = "single.txt"

lines = open(file_path).read().splitlines()
displays = []


for line in lines:
    split   = line.split(' | ')
    data    = split[0].split(' ')
    output  = split[1].split(' ')
    displays.append([data, output])

count = 0
for data, output in displays:
    for digit in output:
        if len(digit) in [2, 4, 3, 7]:
            count += 1


print("Part 1:", count)
