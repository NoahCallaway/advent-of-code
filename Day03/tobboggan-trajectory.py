file_path = "slope-input.txt"

with open(file_path) as f:
    slope = f.read().splitlines()
    f.close()

#make slope into 2d list
for i in range(len(slope)):
    slope[i] = list(slope[i])

def count_trees(accross, down):
    i = 0 #row
    j = 0 #column
    trees = 0

    while i < len(slope):
        if slope[i][j] == '#':
            trees += 1
        i += down
        j += accross
        #wrap around columns if out of range
        if j > (len(slope[0]) - 1):
            j -= (len(slope[0]))

    return trees


directions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
final_answer = 1

for each in directions:
    result = count_trees(each[0], each[1])
    final_answer = final_answer * result
    print("For right %s, down %s. You hit %s trees" % (each[0],each[1],result))

print("Final Answer is %s" % final_answer)
