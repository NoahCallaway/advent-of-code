file_path = "input.txt"
data = open(file_path).read().splitlines()
for i, line in enumerate(data):
    data[i] = list(line.replace(" ",""))

def do_math(line):
    solution = 0

    #remove all + 
    line = solve_addition(line)

    for i, val in enumerate(line):
        if val == "*":
            solution *= int(line[i+1])
    
        elif i == 0:
            solution = int(val)
    return solution

def find_bracket(line):
    bracket_found = False
    bracket_pos = {'start': None, 'end': None}
    
    for i, val in enumerate(line):
        if "(" in val:
            bracket_found = True
            bracket_pos["start"] = i
        if ")" in val and bracket_found == True:
            bracket_pos["end"] = i
            break
    
    if bracket_found == True:
        section = line[bracket_pos["start"]+1:bracket_pos["end"]]
        info = { "start":  bracket_pos["start"], "end": bracket_pos["end"],
                    "section": section}
        return info
    
    return False

def solve_brackets(line):

    bracket = find_bracket(line)
    while bracket:

        solution = do_math(bracket["section"])

        del line[bracket["start"]:bracket["end"]+1]
        line.insert(bracket["start"], str(solution))
        bracket = find_bracket(line)
    return line

def solve_addition(line):
    new_line = []

    for i in range(len(line)):
        if line[i-1] == "+":
            continue
        if line[i] == "+":
            last = int(new_line.pop(-1))
            new_line.append(str( last + int(line[i+1])))
            i = i + 2
        else:
            new_line.append(line[i])

    return new_line

def solve_line(line):
    line = solve_brackets(line)
    solve_addition(line)
    return do_math(line)

total = 0
for line in data:
    total += solve_line(line)
    
print("Part 2: ",total)