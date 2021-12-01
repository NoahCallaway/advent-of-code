file_path = "input.txt"
directions = [(x[0],int(x[1:])) for x in open(file_path).read().splitlines()]

way_point = [1,10] #north, east
ship_pos = [0,0]   #north, east

for ins, n in directions:
    if ins == 'N':
        way_point[0] += n
    elif ins == 'S':
        way_point[0] -= n
    elif ins == 'E':
        way_point[1] += n
    elif ins == 'W':
        way_point[1] -= n
    elif ins == 'F':
        ship_pos[0] += n*way_point[0]
        ship_pos[1] += n*way_point[1]
    elif ins == 'R':
        for i in range(int(n/90)):
            new_way = [-way_point[1],way_point[0]]
            way_point = new_way
    elif ins == 'L':
        for i in range(int(n/90)):
            new_way = [way_point[1],-way_point[0]]
            way_point = new_way

print(abs(ship_pos[0])+abs(ship_pos[1]))