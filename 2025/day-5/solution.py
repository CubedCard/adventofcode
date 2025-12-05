ing_text, ids_text = open("data.txt").read().strip().split("\n\n")


def part1():
    ranges = []
    for line in ing_text.splitlines():
        x, y = line.split("-")
        ranges.append((int(x), int(y)))
    total = 0

    for line in ids_text.splitlines():
        val = int(line)
        for x, y in ranges:
            if x <= val <= y:
                total += 1
                break
    return total


def part2():
    ranges = []
    for line in ing_text.splitlines():
        x, y = map(int, line.split("-"))
        ranges.append((x, y))

    ranges.sort()

    merged = []
    for start, end in ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    total = sum(end - start + 1 for start, end in merged)
    return total


print("Part 1:", part1())
print("Part 2:", part2())