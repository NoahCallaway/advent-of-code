file_path = "test.txt"

assignments = [list(line.split(',')) for line in open(file_path).read().splitlines()]

def create_set(assignment):
    start, end = assignment.split('-')
    return {i for i in  range(int(start), int(end) + 1)}

count_pt1 = 0
count_pt2 = 0
for x, y in assignments:
    first  = create_set(x)
    second = create_set(y)

    if first.issubset(second) or second.issubset(first):
        count_pt1 += 1
    
    #Part 2
    if min(first) <= max(second) and min(second) <= min(first):
        count_pt2 += 1
    elif min(second) <= max(first) and min(first) <= min(second):
        count_pt2 += 1

print("Part 1:", count_pt1)
print("Part 2:", count_pt2)