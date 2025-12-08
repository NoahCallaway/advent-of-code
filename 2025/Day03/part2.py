file_path = "data.txt"

file = open(file_path).read().splitlines()


def find_max_in_range(bank: list, left_limit: int, right_limit: int) -> tuple:
    scoped_bank = bank[left_limit:right_limit]
    max_value = max(scoped_bank)
    index = scoped_bank.index(max_value) + left_limit
    return index, max_value


def find_max_joltage(bank: list) -> int:
    bank_length = len(bank)
    values = []
    left_limit = 0
    for i in range(12, 0, -1):
        right_limit = bank_length - i + 1
        index, max_value = find_max_in_range(bank, left_limit, right_limit)
        left_limit = index + 1
        values.append(max_value)

    max_joltage = int("".join([str(i) for i in values]))
    return max_joltage


sum = 0
for bank in file:
    bank = [int(i) for i in bank]
    sum += find_max_joltage(bank)

print(sum)
