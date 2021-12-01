import re
file_path = "input.txt"
prog = open(file_path).read().splitlines()


def apply_mask(mask: str, binary: list) -> int:
    for i, bit in enumerate(mask):
        if bit == 'X':
            continue
        elif bit == '0':
            binary[i] = '0'
        elif bit == '1':
            binary[i] = 1

    binary = ''.join(map(str, binary))
    return(int(binary,2))

#Part 1
mask = ''
mem = {}
for ins in prog:
    if 'mask' in ins:
        mask = ins.replace('mask = ','')
        continue
    mem_addr = re.findall(r"\[(\d+)\]", ins)[0]
    
    num = int(ins.split(' = ')[1])
    
    #Num to binary and add leading 0's
    binary = list(bin(num).replace('0b',''))
    for i in range(36 - len(binary)):
        binary.insert(0,'0')

    mem[mem_addr] = apply_mask(mask, binary)

sum = 0
for each in mem:
    sum += mem[each]
print(sum)
