from collections import Counter

def parse_input(file):
    return list(map(int, open(f'{file}.txt').read().strip().split()))

def part_1(file):
    stones = parse_input(file)
    return blink(stones, 25)

def part_2(file):
    stones = parse_input(file)
    return blink(stones, 75)

def blink(stones, steps):
    counts = Counter(stones)
    for _ in range(steps):
        next_counts = Counter()
        for stone, count in counts.items():
            stone_str = str(stone)
            if stone == 0:
                next_counts[1] += count
            elif len(stone_str) % 2 == 0:
                mid = len(stone_str) // 2
                next_counts[int(stone_str[:mid])] += count
                next_counts[int(stone_str[mid:])] += count
            else:
                next_counts[stone * 2024] += count
        counts = next_counts

    return sum(counts.values())

print(f'Part 1: {part_1("data")}')
print(f'Part 2: {part_2("data")}')