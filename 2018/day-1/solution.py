data = [line.strip() for line in open('data.txt')]

def part_1():
    return sum([eval(line) for line in data])

def part_2():
    total = 0
    totals = set()
    while True:
        for line in data:
            total += eval(line)
            if total in totals:
                return total
            totals.add(total)
    return None

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")