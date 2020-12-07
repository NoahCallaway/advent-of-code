import re
file_path = "bags-input.txt"

with open(file_path) as f:
    rules = f.read().splitlines()
    f.close()

def data_to_dict(data: list) -> dict:
    x = {}
    for line in data:
        line = re.findall(r'(\D*) bag', line)
        if 'contain no other' in line[0]:
            x[line[0].replace(' bags contain no other','')] = None
        else:
            x[line[0]] = ''.join(line[1:])
    return x

#Part 1
colours = ['shiny gold']
contains = data_to_dict(rules)
def part1():
    start_count = len(colours)

    for bag in contains:
        if contains[bag] != None:
            if bag not in colours:
                for each in colours:
                    if each in contains[bag]:
                        colours.append(bag)
                        break
    if start_count != len(colours):
        part1()

part1()        
print("Part 1 = %s" % (len(colours)-1))

#Part2
def part2(numb_col: tuple) -> int:
    count = int(numb_col[0])
    colour = numb_col[1]
    inside = []
    for bag in rules:
        if bag.startswith(colour):
            inside.extend(bag.split(' contain ')[1].replace('.','').split(', '))
    if 'no other bags' in inside:
        return count
    for each in inside:
        count = count + int(numb_col[0]) * part2(each.split(" ",1))
    return count

print(part2((1,'shiny gold')) - 1)


