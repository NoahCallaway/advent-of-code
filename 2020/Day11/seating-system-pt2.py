file_path = "input.txt"
seats = open(file_path).read().splitlines()

#2D Array for seats
for i, s in enumerate(seats):
    seats[i] = list(s)

def extend_direction(pos: tuple, seats: list, co: tuple):
    i,j = pos[0]+co[0], pos[1]+co[1]
    if i >= 0 and i < len(seats):
        if j >= 0 and j < len(seats[0]):
            if seats[i][j] == '#':
                return '#'
            elif seats[i][j] == 'L':
                return 'L'
            elif seats[i][j] == '.':
                return extend_direction((i,j),seats,co)
    else:
        return None

def apply_rules(seats: list) -> list:
    new_seats = [[None]*len(seats[0]) for i in range(len(seats))]
    coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] #in i,j
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            surrounding = []
            for co in coords:
                surrounding.append(extend_direction((i,j),seats,co))
            if seat == 'L' and '#' not in surrounding:
                new_seats[i][j] = '#'
            elif seat == '#' and surrounding.count('#') >= 5:
                new_seats[i][j] = 'L'
            else:
                new_seats[i][j] = seat
    return new_seats

def part2(seats: list) -> int:
    #Occupied counts
    before = sum([i.count('#') for i in seats])    
    applied = apply_rules(seats)
    after = sum(j.count('#') for j in applied)

    if before == after:
        return after
    else:
        return part2(applied)

print(part2(seats))