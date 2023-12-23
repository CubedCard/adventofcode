import sys

trail = []

sys.setrecursionlimit(100000)


for line in open('data.txt'):
    trail.append(list(line.strip()))

def find_start():
    for i, step in enumerate(trail[0]):
        if step == '.':
            return (0, i)

def find_end():
    for i, step in enumerate(trail[-1]):
        if step == '.':
            return (len(trail) - 1, i)

def prints():
    for line in trail:
        print(''.join(line))

def longest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    
    def is_valid(x, y, visited):
        return 0 <= x < rows and 0 <= y < cols and not visited[x][y] and grid[x][y] in {'.', '>', '<', '^', 'v'}
    
    def get_direction(x, y):
        return grid[x][y]

    def dfs(x, y, visited, path_length):
        nonlocal max_length
        visited[x][y] = True
        path_length += 1

        direction = get_direction(x, y)
        if direction == '>':
            dx, dy = (0, 1)
        elif direction == '<':
            dx, dy = (0, -1)
        elif direction == '^':
            dx, dy = (-1, 0)
        elif direction == 'v':
            dx, dy = (1, 0)
        else:
            # If no specific direction symbol, explore in all directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny, visited):
                    dfs(nx, ny, visited, path_length)

        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, visited):
            dfs(nx, ny, visited, path_length)

        visited[x][y] = False  # backtrack
        max_length = max(max_length, path_length)

    max_length = 0
    visited = [[False] * cols for _ in range(rows)]

    start_x, start_y = start
    end_x, end_y = end

    if grid[start_x][start_y] in {'.', '>', '<', '^', 'v'} and grid[end_x][end_y] == '.':
        dfs(start_x, start_y, visited, 0)

    return max_length

start = find_start()
end = find_end()

print(longest_path(trail, start, end) - 1)
