def part1(lines, start_x):
    width = len(lines[0])
    height = len(lines)
    beam_positions = {start_x}
    split_count = 0
    for y in range(1, height):
        new_beam_positions = set()
        for x in beam_positions:
            if lines[y][x] == "^":
                if x > 0:
                    new_beam_positions.add(x - 1)
                if x < width - 1:
                    new_beam_positions.add(x + 1)
                split_count += 1
            else:
                new_beam_positions.add(x)
        beam_positions = new_beam_positions
    return split_count


def find_number_of_timelines(lines, x, y, memo):
    width = len(lines[0])
    height = len(lines)
    if y >= height:
        return 1
    if (x, y) in memo:
        return memo[(x, y)]
    if lines[y][x] == "^":
        left_timelines = (
            find_number_of_timelines(lines, x - 1, y + 1, memo) if x > 0 else 0
        )
        right_timelines = (
            find_number_of_timelines(lines, x + 1, y + 1, memo) if x < width - 1 else 0
        )
        total_timelines = left_timelines + right_timelines
    else:
        total_timelines = find_number_of_timelines(lines, x, y + 1, memo)
    memo[(x, y)] = total_timelines
    return total_timelines


with open("data.txt") as f:
    lines = f.read().splitlines()
start_x = lines[0].index("S")

print(f"Part 1: {part1(lines, start_x)}")
print(f"Part 2: {find_number_of_timelines(lines, start_x, 1, {})}")
