file_path = "data.txt"

file = open(file_path).read().splitlines()

sums = []
for line in file:
    row = [i for i in line.split(" ") if i != ""]
    if len(sums) == 0:
        sums = [[] for i in range(len(row))]
    for idx, i in enumerate(row):
        sums[idx].append(i)

# do math
total = 0
for sum in sums:
    operation = sum.pop(-1)
    numbers = [int(i) for i in sum]
    print(operation, numbers)
    if operation == "+":
        answer = 0
        for i in numbers:
            answer += i
    elif operation == "*":
        answer = 1
        for i in numbers:
            answer = answer * i
    total += answer

print(total)
