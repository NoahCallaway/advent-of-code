file_path = "data.txt"

file = open(file_path).read().splitlines()

ranges = []

for line in file:
    if "-" in line:
        start, end = line.split("-")
        ranges.append([int(start), int(end)])

ranges = sorted(ranges, key=lambda x: x[0])

merged_ranges = [ranges.pop(0)]

for range in ranges:
    if range[0] - 1 <= merged_ranges[-1][1]:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], range[1])
    else:
        merged_ranges.append(range)

fresh_ingredients = 0

for range in merged_ranges:
    start, end = range
    diff = end - start + 1
    fresh_ingredients += diff

print(fresh_ingredients)
