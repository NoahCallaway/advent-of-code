import re
file_path = "input.txt"
prog = open(file_path).read().splitlines()


def apply_mask(mask: str, binary: list) -> list:

    for i, bit in enumerate(mask):
        if bit == '0':
            continue
        elif bit == 'X':
            binary[i] = 'X'
        elif bit == '1':
            binary[i] = 1

    mem_addresses = []
    for i in range(2**binary.count('X')):
        #i become correct bit length binary array
        x_vals = list(bin(i).replace('0b',''))
        for j in range(binary.count('X')-len(x_vals)):
            x_vals.insert(0,'0')

        new_addr = binary.copy()
        for k, each in enumerate(binary):
            if each == 'X':
                new_addr[k] = x_vals[0]
                x_vals.pop(0)
        
        new_addr = ''.join(map(str, new_addr))
        mem_addresses.append(int(new_addr,2))

    return(mem_addresses)

#Part 2
mask = ''
mem = {}
for ins in prog:
    if 'mask' in ins:
        mask = ins.replace('mask = ','')
        continue
    mem_addr = int(re.findall(r"\[(\d+)\]", ins)[0])
    
    num = int(ins.split(' = ')[1])
    
    #mem_addr to binary and add leading 0's
    binary = list(bin(mem_addr).replace('0b',''))
    for i in range(36 - len(binary)):
        binary.insert(0,'0')

    for addr in apply_mask(mask, binary):
        mem[addr] = num

sum = 0
for each in mem:
    sum += mem[each]
print(sum)
