file_path = "data.txt"

left  = []
right = []

for line in open(file_path).read().splitlines():
    x, y = line.split("   ")
    left.append(int(x))
    right.append(int(y))

# Part 1
left.sort()
right.sort()

differences = []

for i in range(len(left)):
    differences.append(abs(left[i] - right[i]))

# Part 2
similarity_score = 0

for i in range(len(left)):
    similarity_score += left[i] * right.count(left[i])

print("Part 1: ", sum(differences))
print("Part 2: ", similarity_score)
