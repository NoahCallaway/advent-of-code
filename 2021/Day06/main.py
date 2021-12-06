file_path = "data.txt"

data = [f.strip('\n').split(',') for f in open(file_path)]
fish = [int(i) for i in data[0]]

# Part 1
fish_part1 = [fish.count(i) for i in range(0, 9)]
print(fish_part1)
for i in range(80):
    fish_part1[(i + 7) % 9] += fish_part1[i % 9]
print(sum(fish_part1))


# Part 2
fish_part2 = [fish.count(i) for i in range(0, 9)]
print(fish_part2)
for i in range(256):
    fish_part2[(i + 7) % 9] += fish_part2[i % 9]
print(sum(fish_part2))
