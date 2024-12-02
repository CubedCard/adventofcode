import itertools

reports = [line.split() for line in open('data.txt')]

def check_line(line):
    asc = int(line[0]) < int(line[1])
    for i in range(len(line) - 1):
        i1, i2 = int(line[i]), int(line[i + 1])
        if asc and i1 > i2:
            return False
        elif not asc and i1 < i2:
            return False
        if abs(i1 - i2) > 3 or abs(i1 - i2) == 0:
            return False
    return True

def part_1():
    return [check_line(line) for line in reports].count(True)

def part_2():
    return sum([1 for line in reports if sum([1 for l in itertools.combinations(line, len(line) - 1) if (check_line(l))]) > 0])

print("Part 1", part_1())
print("Part 2", part_2())

assert part_1() == 220
assert part_2() == 296
