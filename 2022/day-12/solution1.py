grid = []

for line in open('./data.txt'):
    grid.append(line.strip())

def can_move(x, y, direction):
    if direction == 'U':
        return y > 0 and ord(grid[y-1][x]) - ord(grid[y][x]) <= 1
    elif direction == 'D':
        return y < len(grid)-1 and ord(grid[y+1][x]) - ord(grid[y][x]) <= 1
    elif direction == 'L':
        return x > 0 and ord(grid[y][x-1]) - ord(grid[y][x]) <= 1
    elif direction == 'R':
        return x < len(grid[0])-1 and ord(grid[y][x+1]) - ord(grid[y][x]) <= 1
    else:
        return False

def move(x, y, direction):
    if direction == 'U':
        return x, y-1
    elif direction == 'D':
        return x, y+1
    elif direction == 'L':
        return x-1, y
    elif direction == 'R':
        return x+1, y
    else:
        return x, y

def find_start():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return x + 1, y
    return 0, 0

def find_end():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'E':
                return x - 1, y
    return 0, 0

def find_shortest_path():
    x, y = find_start()
    x_end, y_end = find_end()
    visited = set()
    queue = [(int(0), x, y)]
    while queue:
        distance, x, y = queue.pop(0)
        if x == x_end and y == y_end:
            return distance
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for direction in 'UDLR':
            if can_move(x, y, direction):
                new_x, new_y = move(x, y, direction)
                queue.append((distance+1, new_x, new_y))
    return -1

print(find_shortest_path() + 2) # +2 because we start at the second character and end at the second last character
