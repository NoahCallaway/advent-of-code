file_path = "test.txt"

data = [[i for i in line.split(' ')] for line in open(file_path).read().splitlines()]

x = 1
cycle_count = 0
signal_strength = 0
row = ''

check_interval = [ 20, 60, 100, 140, 180, 220 ]

def cycle():
    global cycle_count, signal_strength
    cycle_count += 1
    if cycle_count in check_interval:
        print(cycle_count, x, x * cycle_count)
        signal_strength += x * cycle_count

for i in data:
    if len(i) > 1:
        for j in range(2):
            cycle()
        x = x + int(i[1])
    else:
        cycle()
cycle()

print(signal_strength)