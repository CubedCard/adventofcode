import time

def parse_input(file_path):
    return [line.strip() for line in open(file_path)]

def build_graph(grid):
    rows, cols = len(grid), len(grid[0])
    end_pos = (-1, -1)
    graph = {}

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] in '.SE':
                graph[(row, col)] = []
                if grid[row][col] == 'E':
                    end_pos = (row, col)

    for row, col in graph.keys():
        for drow, dcol in [(0, 1), (1, 0)]:
            neighbor_row, neighbor_col = row + drow, col + dcol
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols and grid[neighbor_row][neighbor_col] != '#':
                graph[(row, col)].append((neighbor_row, neighbor_col))
                graph[(neighbor_row, neighbor_col)].append((row, col))

    return graph, end_pos

def calculate_shortest_paths(graph, target):
    queue = [target]
    distances = {target: 0}

    while queue:
        current_node = queue.pop(0)
        current_distance = distances[current_node]

        for neighbor in graph[current_node]:
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    return distances

def find_reachable_nodes(grid, x, y, max_distance):
    reachable_nodes = []
    for dx in range(-max_distance, max_distance + 1):
        remaining_distance = max_distance - abs(dx)
        for dy in range(-remaining_distance, remaining_distance + 1):
            if dx == dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] in '.SE':
                reachable_nodes.append((nx, ny))
    return reachable_nodes

def calculate_savings(grid, graph, shortest_paths, max_cheat_distance):
    savings_count = 0

    for (row, col) in graph:
        reachable = find_reachable_nodes(grid, row, col, max_cheat_distance)

        for target_row, target_col in reachable:
            move_cost = abs(row - target_row) + abs(col - target_col)
            if (target_row, target_col) in shortest_paths and (row, col) in shortest_paths:
                direct_cost = shortest_paths[(row, col)]
                target_cost = shortest_paths[(target_row, target_col)] + move_cost
                if direct_cost - target_cost >= 100:
                    savings_count += 1

    return savings_count

def main():
    grid = parse_input("data.txt")
    graph, end_position = build_graph(grid)
    shortest_paths = calculate_shortest_paths(graph, end_position)

    start_time = time.time()
    part1_result = calculate_savings(grid, graph, shortest_paths, max_cheat_distance=2)
    mid_time = time.time()
    part2_result = calculate_savings(grid, graph, shortest_paths, max_cheat_distance=20)
    end_time = time.time()

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")
    print(f"Execution time Part 1: {mid_time - start_time:.4f} seconds")
    print(f"Execution time Part 2: {end_time - mid_time:.4f} seconds")

if __name__ == "__main__":
    main()