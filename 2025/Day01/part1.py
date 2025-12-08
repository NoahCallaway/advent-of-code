file_path = "data.txt"
file = open(file_path).read().splitlines()

dial_value = 50
counter = 0
wrap = 100

for line in file:
    direction = line[0]
    increment = int(line[1:])

    if direction == "L":
        increment = -increment
    dial_value = (dial_value + increment) % wrap
    counter += dial_value == 0

print("Part 1: %s" % counter)
