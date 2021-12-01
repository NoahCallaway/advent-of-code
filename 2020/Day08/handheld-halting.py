from copy import deepcopy
file_path = "program-input.txt"

program = open(file_path).read().splitlines()

program = [line.split(' ') for line in program] #[ [oper, arg] ]

def run_program(prog: list) -> bool:
    acc = 0
    has_run = []
    i = 0
    while i < len(prog):
        if prog[i][0] == 'nop':
            i += 1
        elif prog[i][0] == 'acc':
            acc += int(prog[i][1])
            i += 1
        elif prog[i][0] == 'jmp':
            i += int(prog[i][1])
        
        if i in has_run:
            print("Infinite Loop - Accumulator = %s" % acc)
            return False
        has_run.append(i)
    print("Success - Accumulator = %s" % acc)
    return True

#Part 1
run_program(program)

#Part 2
for i in range(len(program)):
    mod_prog = deepcopy(program)

    if mod_prog[i][0] != "nop" and mod_prog[i][0] != "jmp":
        continue

    elif mod_prog[i][0] == "nop":
        mod_prog[i][0] = "jmp"

    elif mod_prog[i][0] == "jmp":
        mod_prog[i][0] = "nop"
    
    if run_program(mod_prog):
        break