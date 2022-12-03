file_path = "data.txt"

rucksacks =  [line for line in open(file_path).read().splitlines()]

def compartments(rucksack):
  return [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]

def priority(char):
  # lower case
  if ord(char) > 97:
    return ord(char) - 96
  # upper case
  else:
    return ord(char) - 38

def part_one():
  total = 0
  for rucksack in rucksacks:
    first, second = compartments(rucksack)
    in_both = ''.join(set(first).intersection(second))
    sum = 0
    for char in in_both:
      sum += priority(char)
    total += sum
  return total

def part_two():
  total = 0
  for i, j in enumerate(rucksacks):
    if i % 3 == 0:
      in_all = ''.join(set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2]))
      sum = 0
      for char in in_all:
        sum += priority(char)
      total += sum
  return(total)

print("Part 1:", part_one())
print("Part 2:", part_two())