file_path = "data.txt"

lines = open(file_path).read().splitlines()

pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
corrupt_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def remove_pairs(data):
    for key, val in pairs.items():
        if "".join([key, val]) in data:
            data = data.replace("".join([key, val]), '')
            return remove_pairs(data)
    return data


illegal = []
incomplete = []
complete_scores = []

for line in lines:
    corrupt = False
    reduced = remove_pairs(line)
    # Corrupt lines (Part 1)
    for c in reduced:
        if c in pairs.values():
            illegal.append(c)
            corrupt = True
            break

    # Incomplete lines (Part 2)
    if not corrupt:
        completion_string = "".join([pairs[key] for key in reduced[::-1]])
        score = 0
        for char in completion_string:
            score *= 5
            score += completion_points[char]
        complete_scores.append(score)

# Answer Part 1
sum = 0
for key, val in corrupt_points.items():
    sum += illegal.count(key) * val
print("Part 1:", sum)

# Answer Part 2
complete_scores = sorted(complete_scores)
mid_point = int((len(complete_scores) - 1)/2)
print("Part 2:", complete_scores[mid_point])
