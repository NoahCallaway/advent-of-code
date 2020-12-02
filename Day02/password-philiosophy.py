import re

file_path = "password-input.txt"

#get file into list of lines
with open(file_path) as f:
    passwords = f.read().splitlines()
    f.close()

#task 1
def part1():
    valid = 0
    regex = r"(\d*)-(\d*) ([a-z]): (\D*)"

    #Check each line
    for line in passwords:
        (min, max, char, word) = re.findall(regex, line)[0]
        
        occurs = word.count(char)
        if occurs >= int(min) and occurs <= int(max):
            valid += 1

    return valid

#task2
def part2():
    valid = 0
    regex = r"(\d*)-(\d*) ([a-z]): (\D*)"

    #Check each line
    for line in passwords:
        (first, second, char, word) = re.findall(regex, line)[0]
        
        #First and second not the same
        if word[int(first)-1] != word[int(second)-1]:
            #first or second is the character
            if word[int(first)-1] == char or word[int(second)-1] == char:
                valid += 1

    return valid

print("Number of valid Passwords for Part 1 = %s\n" % part1())

print("Number of valid Passwords for Part 2 = %s\n" % part2())