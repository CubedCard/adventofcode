moves = []

for line in open('./data.txt'):
    moves.append(line.strip())

w, h = 1500, 1500
grid = [['.' for x in range(w)] for y in range(h)]

start_pos = [int(h / 2), int(w / 2)]
grid[start_pos[0]][start_pos[1]] = 's'

def print_grid():
    output = ''
    for row in grid:
        output += ''.join(row) + '\n'
    print(output)

head_pos = start_pos.copy()
tail_pos = start_pos.copy()

def head_touches_tail(head_pos, tail_pos):
    return abs(head_pos[0] - tail_pos[0]) <= 1 and abs(head_pos[1] - tail_pos[1]) <= 1

def move_head(direction, times):
    if direction == 'U':
        for _ in range(times):
            head_pos[1] -= 1
            if not head_touches_tail(head_pos, tail_pos):
                grid[tail_pos[0]][tail_pos[1]] = '#'
                tail_pos[0] = head_pos[0]
                tail_pos[1] -= 1
                grid[tail_pos[0]][tail_pos[1]] = 'T'
    elif direction == 'D':
        for _ in range(times):
            head_pos[1] += 1
            if not head_touches_tail(head_pos, tail_pos):
                grid[tail_pos[0]][tail_pos[1]] = '#'
                tail_pos[0] = head_pos[0]
                tail_pos[1] += 1
                grid[tail_pos[0]][tail_pos[1]] = 'T'
    elif direction == 'L':
        for _ in range(times):
            head_pos[0] -= 1
            if not head_touches_tail(head_pos, tail_pos):
                grid[tail_pos[0]][tail_pos[1]] = '#'
                tail_pos[0] -= 1
                tail_pos[1] = head_pos[1]
                grid[tail_pos[0]][tail_pos[1]] = 'T'
    elif direction == 'R':
        for _ in range(times):
            head_pos[0] += 1
            if not head_touches_tail(head_pos, tail_pos):
                grid[tail_pos[0]][tail_pos[1]] = '#'
                tail_pos[0] += 1
                tail_pos[1] = head_pos[1]
                grid[tail_pos[0]][tail_pos[1]] = 'T'

for move in moves:
    direction, times = move.split(' ')
    times = int(times)
    move_head(direction, times)

print_grid()

total = sum(x.count('#') for x in grid)
print(total + 1) # the 1 is for s
