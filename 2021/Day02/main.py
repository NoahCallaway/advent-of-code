file_path = "data.txt"

lines = open(file_path).read().splitlines()

def part1():
    directions = {}

    for line in lines:
        dir, val = line.split(' ')
        
        if dir in directions:
            directions[dir] += int(val)
        else:
            directions[dir] = int(val)

    horizontal = directions['forward']
    depth      = directions['down'] - directions['up']

    return(horizontal * depth)

def part2():
    aim   = 0
    hor   = 0
    depth = 0

    for line in lines: 
        dir, val = line.split(' ')
        val = int(val)

        if dir == 'down':
            aim   += val

        elif dir == 'up':
            aim   -= val
        
        elif dir == 'forward':
            hor   += val
            depth += (aim * val)
    
    return(hor * depth)

print("Part 1", part1())
print("Part 2", part2())