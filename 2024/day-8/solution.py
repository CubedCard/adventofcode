from itertools import combinations

data = [list(line) for line in open("data.txt").read().strip().split("\n")]

def parse_antenna(data):
    antenna = {}
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell != '.':
                antenna.setdefault(cell, []).append((r, c))
    return antenna

def find_antinodes(antenna, data, part2=False):
    antinodes = set()
    width, height = len(data[0]), len(data)
    offset_start, offset_end = (1, 2) if not part2 else (-1, len(data))
    
    for positions in antenna.values():
        for (ar, ac), (br, bc) in combinations(positions, 2):
            dr, dc = ar - br, ac - bc
            for i in range(offset_start, offset_end):
                if 0 <= ar + i * dr < height and 0 <= ac + i * dc < width:
                    antinodes.add((ar + i * dr, ac + i * dc))
                if 0 <= br - i * dr < height and 0 <= bc - i * dc < width:
                    antinodes.add((br - i * dr, bc - i * dc))
    return len(antinodes)

def part_1():
    return find_antinodes(antenna, data)

def part_2():
    return find_antinodes(antenna, data, part2=True)

antenna = parse_antenna(data)

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
