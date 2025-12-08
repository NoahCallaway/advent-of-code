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

    dist = (wrap - dial_value) if increment > 0 else dial_value or wrap

    if abs(increment) >= dist:
        counter += 1 + (abs(increment) - dist) // wrap
    dial_value = (dial_value + increment) % wrap

print("Part 2: %s" % counter)
