import copy
file_path = "data.txt"

file = [line for line in open(file_path).read().splitlines()]

def read_stacks(file):
    # start of list is top of stack
    stacks = {}
    for line in file:
        if '[' in line:
            pointer = 1
            stack = 1
            while pointer < len(line):
                if (char := line[pointer]) != ' ':
                    if stack in stacks:
                        stacks[stack].append(char)
                    else:
                        stacks[stack] = [char]
                pointer += 4
                stack += 1
        else:
            break
    return stacks

def read_moves(file):
    moves = []
    for line in file:
        if 'move' in line:
            _, count, _, source, _, destination =  line.split(' ')
            moves.append([int(count), int(source), int(destination)])
    return(moves)

def part1(moves, stacks):
    for count, source, destination in moves:
        for _ in range(count):
            stacks[destination].insert(0, stacks[source].pop(0))
    
    top_items = ''
    for key in range(1, len(stacks) + 1):
        top_items += stacks[key][0]

    return top_items

def part2(moves, stacks):
    for count, source, destination in moves:
        queue = stacks[source][0:count] # items to move
        stacks[source] = stacks[source][count:] # remove from source
        stacks[destination] = queue + stacks[destination] # add to destination
        print(queue)
        print(stacks[source])
        print(stacks[destination])

    
    top_items = ''
    for key in range(1, len(stacks) + 1):
        top_items += stacks[key][0]

    return top_items

stacks = read_stacks(file)
moves = read_moves(file)

print("Part 1:", part1(moves, copy.deepcopy(stacks)))
print("Part 2:", part2(moves, copy.deepcopy(stacks)))