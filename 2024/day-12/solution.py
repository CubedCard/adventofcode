from collections import defaultdict

def parse_input(file):
    return [list(line) for line in open(f'{file}.txt').read().split()]

def init_area(data):
    width, height = len(data[0]), len(data)
    connected_components = [[0] * width for _ in range(height)]
    visited = {}
    return width, height, connected_components, visited

def dfs(data, width, height, connected_components, visited, x, y, number_of_connected_components):
    if (x, y) in visited:
        return

    visited[(x, y)] = True
    connected_components[y][x] = number_of_connected_components

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and data[ny][nx] == data[y][x]:
            dfs(data, width, height, connected_components, visited, nx, ny, number_of_connected_components)

def build_connected_components(data):
    width, height, connected_components, visited = init_area(data)
    number_of_connected_components = 0

    for y in range(height):
        for x in range(width):
            if (x, y) not in visited:
                dfs(data, width, height, connected_components, visited, x, y, number_of_connected_components)
                number_of_connected_components += 1

    return width, height, connected_components, number_of_connected_components

def get(connected_components, width, height, x, y):
    if 0 <= x < width and 0 <= y < height:
        return connected_components[y][x]
    return -1

def calculate_metrics(data, width, height, connected_components, number_of_connected_components):
    area = defaultdict(int)
    perimeter = defaultdict(int)
    corners = defaultdict(int)

    for y in range(height):
        for x in range(width):
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                a, b, c, d = (
                    get(connected_components, width, height, x, y),
                    get(connected_components, width, height, x + dx, y),
                    get(connected_components, width, height, x, y + dy),
                    get(connected_components, width, height, x + dx, y + dy),
                )
                if (a != b and a != c) or (a == b == c and a != d):
                    corners[a] += 1

            k = 4
            a, b, c = get(connected_components, width, height, x, y), get(connected_components, width, height, x - 1, y), get(connected_components, width, height, x, y - 1)
            if a == b:
                k -= 2
            if a == c:
                k -= 2

            area[a] += 1
            perimeter[a] += k

    return area, perimeter, corners

def part_1_and_2(file):
    data = parse_input(file)
    width, height, connected_components, number_of_connected_components = build_connected_components(data)
    area, perimeter, corners = calculate_metrics(data, width, height, connected_components, number_of_connected_components)

    part1 = sum(area[x] * perimeter[x] for x in area)
    part2 = sum(area[x] * corners[x] for x in area)

    return part1, part2

if __name__ == "__main__":
    part1, part2 = part_1_and_2("data")
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")