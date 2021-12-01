file_path = "input.txt"
vals, tickets = open(file_path).read().split("\nnearby tickets:\n")
vals, mytick = vals.split("\nyour ticket:\n")

vals = vals.splitlines()
mytick = [int(x) for x in mytick.splitlines()[0].split(',')]
tickets = [list(map(int, x.split(','))) for x in tickets.splitlines()]

allowed = {}
all_allowed = []
for val in vals:
    index = val.split(':')[0]
    val = val.split(' ')
    valid = []
    for each in val:
        if '-' in each:
            valid.extend(range(int(each.split('-')[0]),int(each.split('-')[1])+1))
    allowed[index] = valid
    all_allowed.extend(valid)

sum = 0
valid_tickets = []
for ticket in tickets:
    valid = True
    for val in ticket:
        if val not in all_allowed:
            sum += val
            valid = False

    if valid:
        valid_tickets.append(ticket)

print("Part1: ",sum)

valid_tickets.append([int(x) for x in mytick])

def find_poss_positions(allowed: dict, tickets: list) -> dict:
    poss = { x: [] for x in allowed}
    #for each rule
    for key in allowed:
        #for each column
        for j in range(0,len(tickets[0])):
            okay = True
            #for each row
            for i in range(len(tickets)):
                val = tickets[i][j]
                if val in allowed[key]:
                    okay = True if okay != False else okay
                else:
                    okay = False  
            #verify column
            if okay == True:
                poss[key].append(j)
    return poss

#remove singles and repeat
def solve_positions(possible_positions: dict) -> dict:
    positions = dict()      #map key to pos { 'field': ticket-index }
    keys = list(possible_positions.keys()) # unsolved
    while keys:
        for key in keys:
            if len(possible_positions[key]) == 1:
                positions[key] = possible_positions[key][0]
                keys.remove(key)
                #remove index possibility from all unsolved
                for pos in keys:
                    if positions[key] in possible_positions[pos]:
                        possible_positions[pos].remove(positions[key])
                continue
    return positions

possible_pos = find_poss_positions(allowed, valid_tickets)
solved = solve_positions(possible_pos)

ans = 1
for key in solved:
    if 'dep' in key:
        ans = ans * mytick[solved[key]]
print("Part2:",ans)
