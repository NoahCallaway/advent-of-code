file_path = "data.txt"

reports = []
for line in open(file_path).read().splitlines():
    reports.append([int(i) for i in line.split(" ")])

def valid_direction(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        return True
    return False

def check_diffs(report):
    diffs = [abs(report[i] - report[i+1]) for i in range(len(report) - 1)]
    if max(diffs) <= 3 and min(diffs) >= 1:
        return True
    return False

def dampener(report):
    for i, _ in enumerate(report):
        dampened_report = report.copy()
        dampened_report.pop(i)
        print(dampened_report)
        if valid_direction(dampened_report) and check_diffs(dampened_report):
            print("safe")
            return True
    return False



safe_reports = 0
safe_reports_part2 = 0

for report in reports:

    if valid_direction(report) and check_diffs(report):
        safe_reports += 1
    elif dampener(report):
        safe_reports_part2 += 1


print("Part 1:", safe_reports)
print("Part 2: ", safe_reports + safe_reports_part2)


