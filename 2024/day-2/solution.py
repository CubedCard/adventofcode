import itertools

reports = []

for line in open('data.txt'):
    reports.append(line.split())

def check_line(line):
    asc = int(line[0]) < int(line[1])
    for i in range(len(line) - 1):
        i1 = int(line[i])
        i2 = int(line[i + 1])
        if asc: 
            if i1 > i2:
                return False
        else:
            if i1 < i2:
                return False
        if abs(i1 - i2) > 3 or abs(i1 - i2) == 0:
            return False
    return True

def part_1():
    safe = []
    for line in reports:
        safe.append(check_line(line))
    return safe.count(True)

def part_2():
    safe_reports = 0
    for line in reports:
        lines = itertools.combinations(line, len(line) - 1)
        safe = []
        for l in lines:
            safe.append(check_line(l))
        if sum([1 for x in safe if x]) > 0:
            safe_reports += 1
    return safe_reports

print("Part 1", part_1())
print("Part 2", part_2())
