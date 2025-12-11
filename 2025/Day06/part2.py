file_path = "data.txt"

file = open(file_path).read().splitlines()

as_grid = [list(line) for line in file]

# put the operator first
operators = as_grid.pop(-1)
as_grid.insert(0, operators)


def get_column(grid, index):
    return [row[index] for row in grid]


total = 0
numbers = []

for i in range(1, len(as_grid[0]) + 1):
    idx = -i

    column = get_column(as_grid, idx)
    operator = column[0]
    number_string = "".join(column[1:])
    if number_string.isspace():
        continue
    numbers.append(int(number_string))

    if operator == " ":
        continue
    elif operator == "+":
        answer = 0
        for i in numbers:
            answer += i
    elif operator == "*":
        answer = 1
        for i in numbers:
            answer = answer * i
    numbers = []
    total += answer

print(total)


# # do math
# total = 0
# for sum in sums:
#     operation = sum.pop(-1)

#     digit_groups = [[int(j) for j in i] for i in sum]
#     print(digit_groups)
#     exit(0)

#     numbers = [int(i) for i in sum]
#     print(operation, numbers)
#     if operation == "+":
#         answer = 0
#         for i in numbers:
#             answer += i
#     elif operation == "*":
#         answer = 1
#         for i in numbers:
#             answer = answer * i
#     total += answer

# print(total)
