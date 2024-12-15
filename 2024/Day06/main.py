file_path = "data.txt"

grid = [list(line) for line in open(file_path).read().splitlines()]

directions = [(-1, 0), (0,1), (1, 0), (0, -1)]

def find_guard(grid):
   for idx_i, i in enumerate(grid):
    for idx_j, j in enumerate(i):
        if j == '^':
            return [idx_i, idx_j] 

def change_direction(directions, direction_idx) -> int:
    direction_idx += 1

    if direction_idx >= len(directions):
        return 0
    return direction_idx

def check_in_bounds(gird, position):
   if position[0] < 0 or position[0] >= len(grid):
      return False
   
   if position[1] < 0 or position[1] >= len(grid[0]):
      return False
   
   return True

def part1(grid):
    direction_idx = 0 # Start by moving up

    patrolled_positions = []
    guard = find_guard(grid)

    while True:

        if guard not in patrolled_positions:
            patrolled_positions.append(guard)

        next_coord = [guard[0] + directions[direction_idx][0], guard[1] + directions[direction_idx][1]]

        if not check_in_bounds(grid, next_coord):
            return len(patrolled_positions) 

        next_char = grid[next_coord[0]][next_coord[1]]

        if next_char == '#':
            direction_idx = change_direction(directions, direction_idx)
            continue
        
        guard = next_coord
    
print(f'Part 1: {part1(grid)}')