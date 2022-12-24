file_path = "data.txt"

data = [[i for i in line.split(' ')] for line in open(file_path).read().splitlines()]

x = 1
cycle_count = 0
signal_strength = 0
row = []

check_interval = [ 20, 60, 100, 140, 180, 220 ]
row_ends = [ 40, 80, 120, 160, 200, 240 ]
current_offset = 0

def render():
    global row, current_offset
    if cycle_count - 1 in row_ends:
        current_offset = cycle_count - 1
        print(''.join(row))
        row = []

    if (cycle_count - 1) - current_offset in range(x-1,x+2):
        row.append('#')
    else:
        row.append('.')


def cycle():
    global cycle_count, signal_strength
    cycle_count += 1
    if cycle_count in check_interval:
        signal_strength += x * cycle_count
    render()

for i in data:
    if len(i) > 1:
        for j in range(2):
            cycle()
        x = x + int(i[1])
    else:
        cycle()
cycle()

print(signal_strength)