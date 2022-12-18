file_path = "data.txt"

data = [[int(tree) for tree in line ] for line in open(file_path).read().splitlines()]

edges = ( len(data) * 2 ) + ( len(data[0]) * 2 ) - 4

height, width = len(data), len(data[0])
maxr, maxc = height - 1, width - 1

def is_visible(i,j):
    tree = data[i][j]

    east  = all(tree > t for t in data[i][j + 1:])
    west  = all(tree > t for t in data[i][:j])
    south = all(tree > data[i][j] for i in range(i + 1, len(data)))
    north = all(tree > data[i][j] for i in range(i - 1, -1, -1)) 

    if any((east, west, south, north)):
        return True

def scene_score(i,j):
    tree = data[i][j]

    for east in range(j+1, width):
        if data[i][east] >= tree:
            break
    
    for west in range(j-1, -1, -1):
        if data[i][west] >= tree:
            break

    for south in range(i+1, height):
        if data[south][j] >= tree:
            break
    
    for north in range(i-1, -1, -1):
        if data[north][j] >= tree:
            break

    return (east - j) * (j - west) * (south - i) * (i - north)

count = 0
score = []
for i in range(1, maxr):
    for j in range(1, maxc):
        #Part 1
        if is_visible(i,j):
            count += 1
        #Part 2
        score.append(scene_score(i,j))

print("Part 1:", count + edges)
print("Part 2:", max(score))