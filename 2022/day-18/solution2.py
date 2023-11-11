# to high: 3284 -> 2048

data = set([tuple(map(int, line.split(","))) for line in open('data.txt')])

def getCoveredSides(cords):
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    for x, y, z in cords:
        neighbor_droplets = [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbors]
        sides += len([1 for nd in neighbor_droplets if nd not in data])
    return sides 

def getRealCoverdSides(cords):
    sides = 0
    neighbors = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

    min_x = min(c[0] for c in cords)
    max_x = max(c[0] for c in cords)
    min_y = min(c[1] for c in cords)
    max_y = max(c[1] for c in cords)
    min_z = min(c[2] for c in cords)
    max_z = max(c[2] for c in cords)

    seen = set() | cords

    x_range = range(min_x - 1, max_x + 2)
    y_range = range(min_y - 1, max_y + 2)
    z_range = range(min_z - 1, max_z + 2)

    start = (min_x - 1, min_y - 1, min_z - 1)
    queue = [start]
    seen = set() | cords

    while queue:
        x, y, z = queue.pop(0)

        if (x, y, z) in seen:
            continue

        seen.add((x, y, z))
        neighbor_droplets = [(x + dx, y + dy, z + dz) for dx, dy, dz in neighbors]
        sides += len([1 for nd in neighbor_droplets if nd in cords])

        for nd in neighbor_droplets:
            if nd not in seen and nd[0] in x_range and nd[1] in y_range and nd[2] in z_range:
                queue.append(nd)

    return sides

print(getCoveredSides(data))
print(getRealCoverdSides(data))
