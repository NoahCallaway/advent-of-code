file_path = "input.txt"
data = open(file_path).read().split('\n\n')
raw_rules, messages = data[0].splitlines(), data[1].splitlines()

rules = {}
for rule in raw_rules:
    key, rule = rule.split(': ')
    rules[key] = [x.split(' ') for x in rule.split(' | ')]

def check(rules, rule_no, sect, start):
    rule = rules[rule_no]
    #if letter 
    if rule[0][0][0] == '"':
        return {start + 1} if start < len(sect) and rule[0][0][1] == sect[start] else set()
    else:
        end = set()
        for r in rule:
            buff = {start}
            for i in r:
                temp = set()
                for pos in buff:
                    #cobine possibilities
                    temp = temp | check(rules, i, sect, pos)
                buff = temp
            end = end | buff
        return end

#Part 1
count = 0
for message in messages:
    match_len = [x for x in check(rules,'0', message, 0)]
    if len(match_len) == 1:
        if match_len[0] == len(message):
            count += 1
print(count)


#Part 2
rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42','11','31']]

allowed = 0
for message in messages:
    result = check(rules, '0', message, 0)
    if len(message) in result:
        allowed += 1
print("Part2", allowed)
