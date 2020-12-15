pt1_input = "1,2,16,19,18"

mem = { val:i for i, val in enumerate(list(map(int,pt1_input.split(","))))}

last = 0

target = 30000000

for i in range(len(mem), target-1):
    tmp = last
    if tmp not in mem:
        last = 0
    else:
        last = i - mem[tmp]
    mem[tmp] = i
    #Part1
    if i == 2018:
        print("Part1: ", last)

print("Part2: ", last)

