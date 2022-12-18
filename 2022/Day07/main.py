from functools import lru_cache
from collections import deque, defaultdict

file_path = "data.txt"

data = [line for line in open(file_path).read().splitlines()]

def parse_filesystem(console):
    lines = deque(console)
    fs    = defaultdict(list)
    path  = ()

    while lines:
        line    = lines.popleft().split()
        command = line[1]
        args    = line[2:]

        if command == 'ls':
            while lines and not lines[0].startswith('$'):
                size = lines.popleft().split()[0]

                if size == 'dir':
                    continue

                fs[path].append(int(size))
        else:
            if args[0] == '..':
                path = path[:-1]
            else:
                new_path = path + (args[0],)
                fs[path].append(new_path)
                path = new_path

    return fs


@lru_cache(maxsize=None)
def size_directory(path):
    size = 0
    for each in fs[path]:
        if isinstance(each, int):
            size += each
        else:
            size += size_directory(each)
    return size


fs = parse_filesystem(data)

used = size_directory(('/',))
free = 70000000 - used
need = 30000000 - free

part1 = 0
part2 = []
for path in fs:
    size = size_directory(path)
    if size <= 100000:
        part1 += size
    if size >= need:
        part2.append(size)


print("Part 1:", part1)
print("Part 2:", min(part2))