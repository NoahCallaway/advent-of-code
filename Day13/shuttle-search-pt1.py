file_path = "input.txt"
notes = open(file_path).read().splitlines()

est_dep = int(notes[0])
buses = [int(bus) for bus in notes[1].split(',') if bus != 'x']

found = False
time = est_dep
while found == False:
    for bus in buses:
        if (time / bus).is_integer():
            print('Found')
            print((time-est_dep)*bus)
            found = True
    time += 1

