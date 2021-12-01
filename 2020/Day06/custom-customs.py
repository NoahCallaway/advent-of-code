file_path = "customs-input.txt"

with open(file_path) as f:
    groups = f.read().split('\n\n')
    f.close()

#Part 1 Each Yes
def part_one(forms: list) -> int:
    total = 0
    for i in range(len(forms)):
        response = [None]*26
        forms[i] = forms[i].replace('\n','')

        for char in forms[i]:
            if response[ord(char)-97] == None:
                response[ord(char)-97] = 1 

        total += response.count(1)

    return total

print("Part One = %s" % part_one(groups.copy()))

#Part Two
def part_two(forms: list) -> int:
    total = 0
    for form in forms:
        response = [0]*26
        form = form.split('\n')
        for i in form:
            for char in i:
                response[ord(char)-97] = response[ord(char)-97] + 1
        total += response.count(len(form))
    return total

print("Part Two = %s" % part_two(groups.copy()))

            
