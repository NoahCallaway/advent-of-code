file_path = "data.txt"

file = open(file_path).read().splitlines()

divider = file.index("")

rules = [[int(j) for j in i.split("|")] for i in file[0:divider]]
updates = [[int(j) for j in i.split(",")] for i in file[divider+1:]]

def swap(list, indexes):
    tmp = list[indexes[0]]
    list[indexes[0]] = list[indexes[1]]
    list[indexes[1]] = tmp

def check_update(update, rules):
    for before, page in rules:
        if page in update and before in update:
            idx_page = update.index(page)
            idx_before = update.index(before)

            if idx_before > idx_page:
                return [idx_before, idx_page]
    return True


part1 = 0
part2 = 0

for update in updates:
    valid_update = check_update(update, rules)

    if type(valid_update) == bool:
        part1 += update[int((len(update) - 1) / 2)]
    
    else:
        while type(valid_update) != bool:
            swap(update, valid_update)
            valid_update = check_update(update, rules)

        part2 += update[int((len(update) -1)/2)]

print("Part 1:", part1)
print("Part 2:", part2)
