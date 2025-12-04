rolls = [line.strip() for line in open("data.txt")]


def count_adjacent_at(rolls, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(rolls) and 0 <= c < len(rolls[0]):
            if rolls[r][c] == "@":
                count += 1
    return count


def find_safe_rolls(rolls):
    safe_rolls = []
    for i in range(len(rolls)):
        for j in range(len(rolls[0])):
            if rolls[i][j] == "@":
                adjacent_count = count_adjacent_at(rolls, i, j)
                if adjacent_count < 4:
                    safe_rolls.append((i, j))
    return safe_rolls


def part1():
    safe_rolls = find_safe_rolls(rolls)
    return len(safe_rolls)


def part2():
    total = sum(row.count("@") for row in rolls)
    safe_rolls = find_safe_rolls(rolls)
    while len(safe_rolls) > 0:
        safe_rolls = find_safe_rolls(rolls)
        for i, j in safe_rolls:
            rolls[i] = rolls[i][:j] + "." + rolls[i][j + 1 :]
    return total - sum(row.count("@") for row in rolls)


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")