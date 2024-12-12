file_path = "data.txt"

grid  = [list(line) for line in open(file_path).read().splitlines()]

pattern = list("XMAS")

def get_value(i,j):
    if i < 0 or i >= len(grid):
        return "."
    if j < 0 or j >= len(grid[0]):
        return "."
    return grid[i][j]

def find_xmas(i,j):
    search_ords = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

    count = 0
    # Find MAS
    for offset_i, offset_j in search_ords:
        for idc, c in enumerate("MAS"):
            search_location = (i + offset_i * (idc + 1), j + offset_j * (idc + 1))
            
            if get_value(search_location[0],search_location[1]) == c:
                if c == "S":
                    count += 1
                continue
            else:
                break
    return count            

def is_xmas(i,j):
    dir1 = [(-1,1), (0,0), (1,-1)]
    dir2 = [(1,1), (0,0), (-1,-1)]

    string1 = "".join([get_value(i + offset_i, j + offset_j) for offset_i, offset_j in dir1])
    string2 = "".join([get_value(i + offset_i, j + offset_j) for offset_i, offset_j in dir2])

    if (string1 == "MAS" or string1 == "SAM") and (string2 == "MAS" or string2 == "SAM"):
        return True

    return False 
                      


part1 = 0
part2 = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == 'X':
            part1 += find_xmas(i,j)
        if char == 'A':
            part2 += is_xmas(i,j)
            

print("Part 1:", part1)
print("Part 2:", part2)

# Find the gradient then follow it 