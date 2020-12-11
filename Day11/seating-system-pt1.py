file_path = "input.txt"
seats = open(file_path).read().splitlines()

#2D Array for seats
for i, s in enumerate(seats):
    seats[i] = list(s)

def apply_rules(seats: list) -> list:
    new_seats = [[None]*len(seats[0]) for i in range(len(seats))]
    coords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)] #in i,j
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            surrounding = []
            for co in coords:
                if i + co[0] >= 0 and i + co[0] < len(seats):
                    if j + co[1] >= 0 and j + co[1] < len(row):
                        surrounding.append(seats[i+co[0]][j+co[1]])
            if seat == 'L' and '#' not in surrounding:
                new_seats[i][j] = '#'
            elif seat == '#' and surrounding.count('#') >= 4:
                new_seats[i][j] = 'L'
            else:
                new_seats[i][j] = seat
    return new_seats

def part1(seats: list) -> int:
    #Occupied counts
    before = sum([i.count('#') for i in seats])    
    applied = apply_rules(seats)
    after = sum(j.count('#') for j in applied)

    if before == after:
        return after
    else:
        return part1(applied)

print(part1(seats))