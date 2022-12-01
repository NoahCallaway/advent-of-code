file_path = "data.txt"

elf = 0
totals = []

for line in open(file_path).read().splitlines():
  if line != '':
    elf += int(line)
  else:
    totals.append(elf)
    elf = 0

totals.append(elf)
totals.sort()

print("Part 1:", totals[-1])
print("Part 2:", sum(totals[-3:]))
