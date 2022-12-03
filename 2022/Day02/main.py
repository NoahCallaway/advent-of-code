file_path = "data.txt"

plays = [list(line.split(' ')) for line in open(file_path).read().splitlines()]

scores = {
  "X": 1,
  "Y": 2,
  "Z": 3,
}

part_one = {
  "X": { "A": 3, "B": 0, "C": 6}, #rock vs
  "Y": { "A": 6, "B": 3, "C": 0}, #paper vs
  "Z": { "A": 0, "B": 6, "C": 3}  #scissors vs
}

score = 0
for opponent, player in plays:
  score += scores[player] + part_one[player][opponent]

print("Part 1:", score)

# Part 2
part_two = {
  "X": { "A": "Z", "B": "X", "C": "Y", "score": 0}, #loss
  "Y": { "A": "X", "B": "Y", "C": "Z", "score": 3}, #draw
  "Z": { "A": "Y", "B": "Z", "C": "X", "score": 6}  #win
}

score_part_two = 0

for opponent, outcome in plays:
  score_part_two += part_two[outcome]["score"] + scores[part_two[outcome][opponent]]

print("Part 2:", score_part_two)