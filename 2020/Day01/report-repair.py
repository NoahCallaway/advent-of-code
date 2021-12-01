file_location = "report-input.txt"

#Open File
input_file = open(file_location, 'r')

report = []

#Read in each as integer to report
for line in input_file:
    report.append(int(line))
    
#Part One
def part_one():
    for i in report:
        for j in report:
            if (i + j) == 2020:
                print("The Answer is %s x %s = %s" % (i,j,i*j))
                return True

def part_two():
    for i in report:
        for j in report:
            for k in report:
                if (i + j + k) == 2020:
                    print("The Answer is %s x %s x %s = %s" % (i,j,k,i*j*k))
                    return True
part_one()
part_two()