file_path = "data.txt"

file = open(file_path).read().splitlines()


def find_max_joltage(bank: list) -> int:
    digit1 = max(bank[:-1])  # don't include last cell
    digit2 = max(bank[bank.index(digit1) + 1 :])  # from first digit to end
    max_joltage = int(str(digit1) + str(digit2))
    return max_joltage


sum = 0
for bank in file:
    bank = [int(i) for i in bank]
    sum += find_max_joltage(bank)

print(sum)
