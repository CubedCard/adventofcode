from collections import deque

corrupted = [line.strip().split(',') for line in open('data.txt')]

grid = [['.' for x in range(71)] for _ in range(71)]

for i, cor in enumerate(corrupted):
    if i > 1024:
        break
    grid[int(cor[0])][int(cor[1])] = '#'

def shortest_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != '#':
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))
    
    return -1

def part_1(i=1024):
    start = (0, 0)
    goal = (70, 70)

    path_length = shortest_path(grid, start, goal)
    if path_length != -1:
        return path_length
    else:
        return i

def part_2():
    for i, cor in enumerate(corrupted):
        if i > 1024:
            valid = part_1(i)
            if valid == i:
                return corrupted[i - 1][0], corrupted[i - 1][1]
        grid[int(cor[0])][int(cor[1])] = '#'
    return None

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")