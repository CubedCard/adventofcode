grid = []

for line in open('data.txt'):
    grid.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def follow_beam(x, y, direction, grid):
    energized = set()
    stack = [(x, y, direction)]

    while stack:
        x, y, direction = stack.pop()
        
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or ((x, y), direction) in energized:
            continue

        energized.add(((x, y), direction))

        if grid[y][x] == ".":
            if direction == 'up':
                stack.append((x, y - 1, direction))
            elif direction == 'right':
                stack.append((x + 1, y, direction))
            elif direction == 'down':
                stack.append((x, y + 1, direction))
            elif direction == 'left':
                stack.append((x - 1, y, direction))
        elif grid[y][x] == "|":
            if direction == 'right' or direction == 'left':
                stack.append((x, y - 1, 'up'))
                stack.append((x, y + 1, 'down'))
            elif direction == 'up':
                stack.append((x, y - 1, 'up'))
            elif direction == 'down':
                stack.append((x, y + 1, 'down'))
        elif grid[y][x] == "-":
            if direction == 'up' or direction == 'down':
                stack.append((x - 1, y, 'left'))
                stack.append((x + 1, y, 'right'))
            elif direction == 'left':
                stack.append((x - 1, y, 'left'))
            elif direction == 'right':
                stack.append((x + 1, y, 'right'))
        elif grid[y][x] == "/":
            if direction == 'up':
                stack.append((x + 1, y, 'right'))
            elif direction == 'right':
                stack.append((x, y - 1, 'up'))
            elif direction == 'down':
                stack.append((x - 1, y, 'left'))
            elif direction == 'left':
                stack.append((x, y + 1, 'down'))
        elif grid[y][x] == "\\":
            if direction == 'up':
                stack.append((x - 1, y, 'left'))
            elif direction == 'right':
                stack.append((x, y + 1, 'down'))
            elif direction == 'down':
                stack.append((x + 1, y, 'right'))
            elif direction == 'left':
                stack.append((x, y - 1, 'up'))

    return energized

def part1(x, y, direction):
    copy_grid = [row[:] for row in grid]
    energized = follow_beam(x, y, direction, copy_grid)

    for (x, y), direction in energized:
        copy_grid[y][x] = '#'

    return sum([row.count('#') for row in copy_grid])

def part2():
    max_energized = 0
    for x in range(len(grid[0])):
        max_energized = max(max_energized, part1(x, 0, 'down'))
        max_energized = max(max_energized, part1(x, len(grid) - 1, 'up'))
    for y in range(len(grid)):
        max_energized = max(max_energized, part1(0, y, 'right'))
        max_energized = max(max_energized, part1(len(grid[0]) - 1, y, 'left'))
    return max_energized

print("Part 1:", part1(0, 0, 'right'))
print("Part 2:", part2())
