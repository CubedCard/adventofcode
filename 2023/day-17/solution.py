grid = []

for line in open('ex.txt'):
    grid.append(list(line.strip()))

start = (0, 0)
end = (len(grid[0]) - 1, len(grid) - 1)

def get_neighbors(curr):
    x, y = curr
    neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    neighbors = [neighbor for neighbor in neighbors if neighbor[0] >= 0 and neighbor[0] < len(grid[0]) and neighbor[1] >= 0 and neighbor[1] < len(grid)]

    return neighbors

def get_direction(curr, neighbor):
    x, y = curr
    nx, ny = neighbor
    if x == nx:
        if y < ny:
            return 'D'
        else:
            return 'U'
    if y == ny:
        if x < nx:
            return 'R'
        else:
            return 'L'

def is_oposite_direction(curr, neighbor, direction):
    x, y = curr
    nx, ny = neighbor
    if direction == 'D' or direction == 'U':
        return x == nx
    if direction == 'L' or direction == 'R':
        return y == ny

def bfs(start, end):
    queue = [(start, None, 0)] # (node, direction, distance traveled in this direction)
    visited = set()
    visited.add(start)
    dist = {start: 0}
    path = {start: None}

    while queue:
        curr, direction, distance = queue.pop(0)
        if curr == end:
            return dist[curr], path

        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                if distance > 2 and (is_oposite_direction(curr, neighbor, direction) or direction == get_direction(curr, neighbor)):
                    continue
                new_direction = get_direction(curr, neighbor)
                new_distance = distance
                if direction == new_direction:
                    new_distance += 1
                else: 
                    new_distance = 2 
                queue.append((neighbor, new_direction, new_distance))
                visited.add(neighbor)
                dist[neighbor] = dist[curr] + int(grid[neighbor[1]][neighbor[0]])
                path[neighbor] = curr
    return -1, path

def dijkstra(start, destination, grid):
    rows, cols = len(grid), len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    pq = [(0, start, 'R', 0)] # (distance, node, direction, distance traveled in this direction)
    visited = set()
    path = {start: None}

    while pq:
        distance, current, direction, dir_distance  = pq.pop(0)

        if current == destination:
            return distance, path

        if current in visited:
            continue

        visited.add(current)

        x, y = current
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for neighbor in neighbors:
            if distance > 2 and (is_oposite_direction(current, neighbor, direction) or direction == get_direction(current, neighbor)):
                continue
            new_direction = get_direction(current, neighbor)
            new_distance = distance
            if direction == new_direction:
                new_distance += 1
            else: 
                new_distance = 2 
            nx, ny = neighbor
            if is_valid(nx, ny):
                cost = int(grid[nx][ny])
                if neighbor not in visited:
                    pq.append((distance + cost, neighbor, new_direction, new_distance))
                    path[neighbor] = current

    return -1, path

result, path = dijkstra(start, end, grid)
print(result)

current = end
while current:
    x, y = current
    grid[y][x] = 'X'
    current = path[current]

for line in grid:
    print(line)
