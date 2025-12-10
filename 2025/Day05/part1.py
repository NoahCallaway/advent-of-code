file_path = "data.txt"

file = open(file_path).read().splitlines()

ranges = []
available_ids = []

for line in file:
    if "-" in line:
        start, end = line.split("-")
        ranges.append((int(start), int(end)))
    elif len(line) > 0:
        available_ids.append(int(line))

fresh_ingredients = 0

for id in available_ids:
    for start, end in ranges:
        if id >= start and id <= end:
            fresh_ingredients += 1
            break

print(fresh_ingredients)
