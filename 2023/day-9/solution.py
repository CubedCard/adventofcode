histories = []

for line in open('data.txt'):
    values = line.strip().split(' ')
    histories.append(values)

def part1():
    def find_next(history):
        diffs = []
        for i in range(len(history) - 1):
            diffs.append(int(history[i+1]) - int(history[i]))
        if all(d == 0 for d in diffs):
            return history[-1]
        else:
            return int(history[-1]) + find_next(diffs)

    total = 0
    for history in histories:
        total += find_next(history)

    return total

def part2():
    def find_next(history):
        diffs = []
        for i in range(len(history) - 1):
            diffs.append(int(history[i+1]) - int(history[i]))
        if all(d == 0 for d in diffs):
            return history[0]
        else:
            return int(history[0]) - find_next(diffs)

    total = 0
    for history in histories:
        total += find_next(history)

    return total


print(part1())
print(part2())
