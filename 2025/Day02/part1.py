file_path = "data.txt"
file = open(file_path).read().splitlines()[0].split(",")


def expand_range(id_range) -> list:
    id1, id2 = id_range.split("-")
    return range(int(id1), int(id2) + 1)


def is_bad_id(id) -> bool:
    id = str(id)
    l = len(id)
    if l % 2 == 0:
        first_half = id[0 : l // 2]
        second_half = id[l // 2 :]
        if first_half == second_half:
            return True
    return False


bad_id_sum = 0
for id_range in file:
    expanded_range = expand_range(id_range)
    for id in expanded_range:
        bad_id_sum += id if is_bad_id(id) else 0
        bad = is_bad_id(id)

print(bad_id_sum)
