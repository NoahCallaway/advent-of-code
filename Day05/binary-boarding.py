import math
file_path = "boarding-input.txt"

with open(file_path) as f:
    passes = f.read().split('\n')
    f.close()

def binary_partition(min: int, max: int, segment: str) -> tuple:
    mid = min + (max-min)/2

    if segment == 'F' or segment == 'L':
        return (min,math.floor(mid))
    elif segment == 'B' or segment == 'R':
        return (math.ceil(mid), max)

IDS = []
for seat in passes:
    row = seat[:7]
    column = seat[-3:]

    rows = (0,127)
    columns = (0,7)
    for seg in row:
        rows = binary_partition(rows[0],rows[1],seg)
    
    for seg in column:
        columns = binary_partition(columns[0],columns[1],seg)
    
    IDS.append(rows[0]*8 + columns[0])
    
#Part 1 Highest Seat ID
print("Highest Seat ID = %s" % max(IDS))

#Part Two Missing Seat
def find_seat(lowest: int, highest: int) -> int:
    for seat in range(lowest,highest):
        if seat not in IDS:
            if seat - 1 in IDS and seat + 1 in IDS:
                return seat
    
print("Free Seat is: %s" % find_seat(min(IDS), max(IDS)))