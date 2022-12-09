moves = []

for line in open('./data3.txt'):
    moves.append(line.strip())

w, h = 30, 30 
grid = [['.' for x in range(w)] for y in range(h)]

start_pos = [int(h / 2), int(w / 2)]
grid[start_pos[0]][start_pos[1]] = 's'

def print_grid():
    output = ''
    for row in grid:
        output += ''.join(row) + '\n'
    print(output)

head_pos = start_pos.copy()

tails = [start_pos.copy() for _ in range(9)]

def head_touches_tail(pos_1, pos_2):
    return abs(pos_1[0] - pos_2[0]) <= 1 and abs(pos_1[1] - pos_2[1]) <= 1

def move_tail(times, x, y, value):
    for _ in range(times):
        head_pos[x] += value
        for i in range(len(tails)):
            previous_pos = head_pos
            if i != 0:
                previous_pos = tails[i - 1]
            tail_pos = tails[i]
            if not head_touches_tail(previous_pos, tail_pos):
                if i == len(tails) - 1:
                    grid[tail_pos[1]][tail_pos[0]] = '#'
                elif grid[tail_pos[1]][tail_pos[0]] != '#':
                    grid[tail_pos[1]][tail_pos[0]] = '.'
                tail_pos[y] = previous_pos[y]
                tail_pos[x] += value
                if grid[tail_pos[1]][tail_pos[0]] != '#':
                    grid[tail_pos[1]][tail_pos[0]] = str(i + 1)

def move_head(direction, times):
    if direction == 'U':
        move_tail(times, 1, 0, -1)
    elif direction == 'D':
        move_tail(times, 1, 0, 1)
    elif direction == 'L':
        move_tail(times, 0, 1, -1)
    elif direction == 'R':
        move_tail(times, 0, 1, 1)

for move in moves:
    direction, times = move.split(' ')
    times = int(times)
    move_head(direction, times)
    print(direction, times)
    print_grid()
    print()

total = sum(x.count('#') for x in grid)
print(total + 1) # +1 for the starting position 
