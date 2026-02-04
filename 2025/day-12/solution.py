import re


def load_gifts_and_areas(filename="data.txt"):
    with open(filename) as f:
        content = f.read().strip()
    *gift_blocks, areas_block = re.split(r"\r?\n\r?\n", content)
    gifts = [
        sum(1 for c in "".join(block.splitlines()[1:]) if c == "#")
        for block in gift_blocks
    ]
    areas = []
    for line in areas_block.splitlines():
        parts = [int(x) for x in re.split(r"[x: ]+", line)]
        mx, my, counts = parts[0], parts[1], parts[2:]
        areas.append((mx, my, counts))
    return gifts, areas


def fits_count(gifts, areas):
    return sum(
        1
        for mx, my, counts in areas
        if sum(gift * cnt for gift, cnt in zip(gifts, counts)) < mx * my
    )


gifts, areas = load_gifts_and_areas("data.txt")
part1 = fits_count(gifts, areas)
print(f"Part 1: {part1}")
