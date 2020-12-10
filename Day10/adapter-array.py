file_path = 'input.txt'
adapters = [int(x) for x in open(file_path).readlines()]

phone_rating = max(adapters) + 3

sort = sorted(adapters)
sort.append(phone_rating)
sort.insert(0,0)
ones, threes = 0, 0

#Count intervals
for i, val in enumerate(sort):
    if (val - sort[i-1]) == 1:
        ones += 1
    elif (val - sort[i-1]) == 3:
        threes += 1
print("Part 1 = ", ones * threes)

#highest to lowest
sort.sort(reverse=True)
poss = [0]*len(sort)
poss[0] = 1 #last number only 1 possible

def solutions(i: int, num: int):
    if poss[i]:
        return
    total = 0
    for j, m in enumerate(sort):
        if m > num and m <= num + 3:
            total = total + poss[j]
    poss[i] = total

for i, num in enumerate(sort):
    solutions(i,num)
print("Part 2 = ", poss[-1])