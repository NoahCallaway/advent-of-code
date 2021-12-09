from collections import Counter

file_path = 'data.txt'
lines = [list(map(int,line)) for line in open(file_path).read().splitlines()]

around = [(1,0), (0,1), (-1,0), (0,-1)]
height = len(lines)
width = len(lines[0])

lows = []
lows_ords = []

for i in range(height):
    for j in range(width):
        centre = lines[i][j]
        surrounding = [lines[i+off[0]][j+off[1]] for off in around 
            if 0 <= i+off[0] < height and 0 <= j+off[1] < width]
        
        if centre < min(surrounding):
            lows.append(centre) 
            lows_ords.append((i,j))


def basins(map, lows_ords):
    width = len(map[0])
    height = len(map)

    def fill(x, y, value):
        if x < 0 or x >= height:
            return

        if y < 0 or y >= width:
            return

        if map[x][y] == value or map[x][y] == 9 or map[x][y] < 0:
            return

        map[x][y] = value
        fill(x-1, y, value)
        fill(x+1, y, value)
        fill(x, y-1, value)
        fill(x, y+1, value)

    for i, (x, y) in enumerate(lows_ords):
        fill(x, y, (i + 1) * -1)

    c  = Counter()
    for row in map:
        c.update(row)

    del c[9]
    total = 1
    for key, size in c.most_common(3):
        total *= size

    return total


print("Part1:", sum(lows) + len(lows))
print("Part2", basins(lines, lows_ords))
