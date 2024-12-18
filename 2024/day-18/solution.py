from collections import deque

corrupted = [line.strip().split(',') for line in open('data.txt')]

grid = [['.' for x in range(71)] for _ in range(71)]

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
    start, goal = (0, 0), (70, 70)

    path_length = shortest_path(grid, start, goal)
    return path_length if path_length != -1 else i

def add_corruptions(part2=False):
    for i, cor in enumerate(corrupted):
        if i > 1024:
            if part2:
                if part_1(i) == i: 
                    return ",".join((corrupted[i - 1][0], corrupted[i - 1][1]))
            else:
                break
        grid[int(cor[0])][int(cor[1])] = '#'
    return None

add_corruptions()

print(f"Part 1: {part_1()}")
print(f"Part 2: {add_corruptions(True)}")
