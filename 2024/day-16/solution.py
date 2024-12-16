import heapq
from collections import deque

def parse_grid(grid):
    start, end = None, None
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)

    return start, end, rows, cols

def dijkstra(grid, start, end, rows, cols):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start_state = (start[0], start[1], 1)

    pq = []
    heapq.heappush(pq, (0, start_state))
    visited = {start_state: 0}

    while pq:
        cost, (x, y, d) = heapq.heappop(pq)

        if visited.get((x, y, d), float("inf")) < cost:
            continue

        dx, dy = directions[d]
        nx, ny = x + dx, y + dy

        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "#":
            new_cost = cost + 1
            if new_cost < visited.get((nx, ny, d), float("inf")):
                visited[(nx, ny, d)] = new_cost
                heapq.heappush(pq, (new_cost, (nx, ny, d)))

        for nd in [(d - 1) % 4, (d + 1) % 4]:
            turn_cost = cost + 1000
            if turn_cost < visited.get((x, y, nd), float("inf")):
                visited[(x, y, nd)] = turn_cost
                heapq.heappush(pq, (turn_cost, (x, y, nd)))

    return visited

def backtrack_paths(grid, visited, end, rows, cols):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    min_cost = min(visited[(end[0], end[1], d)] for d in range(4) if (end[0], end[1], d) in visited)

    shortest_path_tiles = set()
    queue = deque()

    for d in range(4):
        end_state = (end[0], end[1], d)
        if end_state in visited and visited[end_state] == min_cost:
            shortest_path_tiles.add(end_state)
            queue.append(end_state)

    while queue:
        x, y, d = queue.popleft()
        cost = visited[(x, y, d)]

        dx, dy = directions[d]
        px, py = x - dx, y - dy

        if 0 <= px < rows and 0 <= py < cols and grid[px][py] != "#":
            prev_cost = cost - 1
            if prev_cost >= 0:
                prev_state = (px, py, d)
                if prev_state in visited and visited[prev_state] == prev_cost:
                    if prev_state not in shortest_path_tiles:
                        shortest_path_tiles.add(prev_state)
                        queue.append(prev_state)

        turn_cost = cost - 1000
        if turn_cost >= 0:
            for pd in [(d - 1) % 4, (d + 1) % 4]:
                prev_state = (x, y, pd)
                if prev_state in visited and visited[prev_state] == turn_cost:
                    if prev_state not in shortest_path_tiles:
                        shortest_path_tiles.add(prev_state)
                        queue.append(prev_state)

    return {(x, y) for (x, y, _) in shortest_path_tiles}

def solve_maze(grid):
    start, end, rows, cols = parse_grid(grid)
    visited = dijkstra(grid, start, end, rows, cols)

    part1 = min(visited[(end[0], end[1], d)] for d in range(4) if (end[0], end[1], d) in visited)
    print(f"Part 1: {part1}")

    shortest_path_tiles = backtrack_paths(grid, visited, end, rows, cols)
    print(f"Part 2: {len(shortest_path_tiles)}")

if __name__ == "__main__":
    grid = [list(line.strip()) for line in open("data.txt")]
    solve_maze(grid)