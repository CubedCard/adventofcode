left = []
right = []

for line in open('data.txt'):
    l, r = line.split()
    left.append(l)
    right.append(r)

left.sort()
right.sort()

def part_1():
    return sum([abs(int(l) - int(right[i])) for i, l in enumerate(left)])

def part_2():
    return sum([right.count(l) * int(l) for i, l in enumerate(left)])

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")

assert part_1() == 2264607
assert part_2() == 19457120
