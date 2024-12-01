left = []
right = []

for line in open('data.txt'):
    l, r = line.split()
    left.append(l)
    right.append(r)


def show():
    for i in range(len(left)):
        print(left[i], right[i])

def part_1():
    left.sort()
    right.sort()

    difference = 0

    for i in range(len(left)):
        l = left[i]
        r = right[i]
        difference += abs(int(l) - int(r))

    return difference

def part_2():
    similarity = 0
    for i in range(len(left)):
        l = left[i]
        count = right.count(l)
        similarity += count * int(l)

    return similarity

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
