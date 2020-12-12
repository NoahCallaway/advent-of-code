file_path = "input.txt"
directions = [(x[0],int(x[1:])) for x in open(file_path).read().splitlines()]

poss_dir = ['N', 'E', 'S', 'W']
ship_dir = 1 #start east

north = 0
east = 0

def move_NE(dir: str, dist: int):
    global north, east
    if dir == 'N':
        north += dist
    elif dir == 'S':
        north -= dist
    elif dir == 'E':
        east += dist
    elif dir == 'W':
        east -= dist

for dir, dist in directions:
    if dir in poss_dir:
        move_NE(dir, dist)
    elif dir == 'F':
        move_NE(poss_dir[ship_dir], dist)
    elif dir == 'R':
        new_dir = int(dist/90) + ship_dir
        ship_dir = new_dir if new_dir < len(poss_dir) else new_dir-4
    elif dir == 'L':
        new_dir = ship_dir - int(dist/90)
        ship_dir = new_dir if new_dir >= 0 else new_dir+4

print(abs(east) + abs(north))