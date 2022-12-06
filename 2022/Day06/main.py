file_path = "data.txt"

message = [line for line in open(file_path).read().splitlines()][0]

part1 = False
for i, char in enumerate(message):

  if len(set(message[i:i+4])) == len(message[i:i+4]) and not part1:
    part1 = True
    print("Part1:", i+4)
    
  elif len(set(message[i:i+14])) == len(message[i:i+14]):
    print("Part2:", i+14)
    break