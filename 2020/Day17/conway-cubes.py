file_path = "input.txt"
data = open(file_path).read().splitlines()

def coord_to_key(x, y, z):
    return "%s,%s,%s" % (x,y,z)

def key_to_coord(key):
    split  = [int(x) for x in key.split(',')]
    return { 'x': split[0], 'y': split[1], 'z': split[2] }

def get_neighbour_coords(x, y, z):
    coords = []
    for nx in range(x-1, x+2):
        for ny in range(y-1, y+2):
            for nz in range(z-1, z+2):
                if not (x == nx and y == ny and z == nz):
                    coords.append(coord_to_key(nx, ny, nz))
    return coords

def get_cube_state(x, y, z, matrix):
    key = coord_to_key(x,y,z)

    if key in matrix:
        return matrix[key]
    else:
        return '.'


def find_min_max_coords(matrix):
    min_coord = { 'x': 0, 'y': 0, 'z': 0 }
    max_coord = { 'x': 0, 'y': 0, 'z': 0 }

    for key, val in matrix.items():
        coord = key_to_coord(key)
        cube_state = val

        if cube_state == '#' or True:
            if coord['x'] < min_coord['x']:
                min_coord['x'] = coord['x']
            elif coord['x'] > max_coord['x']:
                max_coord['x'] = coord['x']

            if coord['y'] < min_coord['y']:
                min_coord['y'] = coord['y']
            elif coord['y'] > max_coord['y']:
                max_coord['y'] = coord['y']
            
            if coord['z'] < min_coord['z']:
                min_coord['z'] = coord['z']
            elif coord['z'] > max_coord['z']:
                max_coord['z'] = coord['z']
    
    return { 'min': min_coord, 'max': max_coord }

def count_active(coords, matrix):
    count = 0

    for key in coords:
        coord = key_to_coord(key)
        if get_cube_state(coord['x'], coord['y'], coord['z'], matrix) == '#':
            count += 1
    
    return count
        
def cycle(matrix):
    new_matrix = {}
    min_max = find_min_max_coords(matrix)

    for x in range((min_max['min']['x']) - 1, (min_max['max']['x'] +2)):
        for y in range((min_max['min']['y']) - 1, (min_max['max']['y'] +2)):
            for z in range((min_max['min']['z']) - 1, (min_max['max']['z'] +2)):
                cube_state = get_cube_state(x,y,z, matrix)

                neighbours = get_neighbour_coords(x, y, z)
                active_count = count_active(neighbours, matrix)

                key = coord_to_key(x, y, z)

                if cube_state == '.' and active_count == 3:
                    new_matrix[key] = '#'
                elif cube_state == '#' and (active_count == 2 or active_count == 3):
                    new_matrix[key] = '#'
    return new_matrix

my_matrix = {}
for y, y_val in enumerate(data):
    for x, x_val in enumerate(y_val):
        my_matrix[coord_to_key(x,y,0)] = x_val

def print_matrix(matrix):
    min_max = find_min_max_coords(matrix)
    for z in range(min_max['min']['z'], min_max['max']['z']+1):
        print("z: ",z)
        for y in range(min_max['min']['y'], min_max['max']['y']+1):
            print([get_cube_state(x, y, z, matrix) for x in range(min_max['min']['x'], min_max['max']['x']+1)])



for i in range(6):
    my_matrix = cycle(my_matrix)

count = count_active(my_matrix.keys(), my_matrix)
#print_matrix(my_matrix)
print(count)