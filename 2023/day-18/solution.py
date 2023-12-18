# to low: 43624
# answer: 47675

instructions = []
grid = [['.' for _ in range(390)] for _ in range(390)]

for line in open('data.txt'):
    instruction, value, color = line.strip().split(' ')
    instructions.append((instruction, int(value)))

pos = (0, 0)
path = []
for instruction in instructions:
    if instruction[0] == 'R':
        for i in range(instruction[1]):
            grid[pos[0]][pos[1]] = '#'
            path.append(pos)
            pos = (pos[0], pos[1] + 1)
    elif instruction[0] == 'L':
        for i in range(instruction[1]):
            grid[pos[0]][pos[1]] = '#'
            path.append(pos)
            pos = (pos[0], pos[1] - 1)
    elif instruction[0] == 'U':
        for i in range(instruction[1]):
            grid[pos[0]][pos[1]] = '#'
            path.append(pos)
            pos = (pos[0] - 1, pos[1])
    elif instruction[0] == 'D':
        for i in range(instruction[1]):
            grid[pos[0]][pos[1]] = '#'
            path.append(pos)
            pos = (pos[0] + 1, pos[1])

def is_surrounded(pos):
    found_left, found_right, found_up, found_down = False, False, False, False
    for i in range(0, len(grid)):
        if pos[0] - i >= 0 and grid[pos[0] - i][pos[1]] == '#':
            found_up = True
        if pos[0] + i < len(grid) and grid[pos[0] + i][pos[1]] == '#':
            found_down = True
        if pos[1] - i >= 0 and grid[pos[0]][pos[1] - i] == '#':
            found_left = True
        if pos[1] + i < len(grid) and grid[pos[0]][pos[1] + i] == '#':
            found_right = True
    return found_left and found_right and found_up and found_down

count = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if is_surrounded((i, j)):
            grid[i][j] = '#'
            count += 1

print(sum([sum([1 if x == '#' else 0 for x in row]) for row in grid]))

for line in grid:
    print(''.join(line))

