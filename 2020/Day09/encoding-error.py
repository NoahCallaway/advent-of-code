file_path = "input.txt"
encoded = open(file_path).read().splitlines()

#Part 1
def find_first_error(numbers: list, preamble: int) -> int:
    i = preamble
    while i < len(numbers):
        allowed = []
        for num in numbers[i-preamble:i]:
            allowed.extend([int(num) + int(x) for x in numbers[i-preamble:i] if x != num and int(x)+int(num) not in allowed])
        if int(numbers[i]) not in allowed:
            return int(numbers[i])
        i += 1  

error = find_first_error(encoded, 25)
print(error)

#Part 2 
def find_contiguos(numbers: list, target: int) -> bool:
    for i in range(len(numbers)):
        total = int(numbers[i])
        added = [total]
        x = i + 1
        while total < target:
            total += int(numbers[x])  
            added.append(int(numbers[x])) 
            if total == target:
                return min(added) + max(added)
            x += 1

print(find_contiguos(encoded,error))




