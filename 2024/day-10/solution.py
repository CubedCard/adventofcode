from collections import deque

grid = [[int(x) for x in line.strip()] for line in open('data.txt')]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
rows, cols = len(grid), len(grid[0])

def bfs_count_paths(grid):
    total_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:  
                queue = deque([(r, c)])
                visited = set()
                visited.add((r, c))
                
                while queue:
                    x, y = queue.popleft()

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                            if grid[nx][ny] == grid[x][y] + 1:
                                if grid[nx][ny] == 9:
                                    total_count += 1
                                queue.append((nx, ny))
                                visited.add((nx, ny))

    return total_count

def find_paths(x, y, current_path):
    if grid[x][y] == 9:
        paths.append(current_path[:])
        return

    visited.add((x, y))

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
            current_path.append((nx, ny))  
            find_paths(nx, ny, current_path)
            current_path.pop()  

    visited.remove((x, y))

def get_all_paths():
    global visited, paths
    visited, paths = set(), []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                find_paths(i, j, [(i, j)])

    return paths

print(f'Part 1: {bfs_count_paths(grid)}')
print(f'Part 2: {len(get_all_paths())}')