import numpy as np 

garden = []

for line in open('data.txt'):
    garden.append(list(line.strip()))

def find_start():
    for row in garden:
        for col in row:
            if col == 'S':
                return row.index(col), garden.index(row)

def get_neighbors(x, y):
    neighbors = []
    if x > 0 and garden[y][x-1] != '#':
        neighbors.append((x-1, y))
    if x < len(garden[0])-1 and garden[y][x+1] != '#':
        neighbors.append((x+1, y))
    if y > 0 and garden[y-1][x] != '#':
        neighbors.append((x, y-1))
    if y < len(garden)-1 and garden[y+1][x] != '#':
        neighbors.append((x, y+1))
    return neighbors

def part1(start):
    distances = {(j, i): [] for i, row in enumerate(garden) for j, _ in enumerate(row)}

    distances[start].append(0)

    for i in range(64):
        for node in distances:
            if len(distances[node]) > 0 and distances[node][-1] == i:
                x, y = node
                for neighbor in get_neighbors(x, y):
                    distances[neighbor].append(i+1)

    return len(set([x for x in distances if 64 in distances[x]]))

def part2(start, dis):
    distances = {}
    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distances[start] = []
    distances[start].append(0)

    possibilities = []

    for i in range(dis + 1):
        if (i - 65) % 131 == 0:
            possibilities.append(len([x for x in distances if i in distances[x]]))
        new_distances = {}
        for node in distances:
            if len(distances[node]) > 0 and distances[node][-1] == i:
                x, y = node
                for neighbor in neighbors:
                    nx, ny = x + neighbor[0], y + neighbor[1]
                    new_ny = ny if ny < len(garden) else ny % len(garden)
                    new_nx = nx if nx < len(garden[0]) else nx % len(garden[0])
                    while new_ny < 0:
                        new_ny += len(garden)
                    while new_nx < 0:
                        new_nx += len(garden[0])
                    if garden[new_ny][new_nx] != '#':
                        if (nx, ny) not in new_distances:
                            new_distances[(nx, ny)] = []
                        new_distances[(nx, ny)].append(i+1)
        distances.update(new_distances)
    return possibilities

print(f"Part 1: {part1(find_start())}")
possibilities = part2(find_start(), 65 + 131 * 2)

vander_matrix = np.vander([0, 1, 2], len(possibilities))

coef = np.linalg.solve(vander_matrix, possibilities)

n = 202300
result = int(coef[0] * (n ** 2) + coef[1] * n + coef[2])
print(f"Part 2: {result}")
