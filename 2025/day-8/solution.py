import math
from itertools import combinations


def read_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            points.append((x, y, z))
    return points


def compute_edges(points):
    edges = []
    n = len(points)
    for i, j in combinations(range(n), 2):
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
        edges.append((dist, i, j))
    edges.sort()
    return edges


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def part_1(filename):
    points = read_points(filename)
    edges = compute_edges(points)
    n = len(points)

    uf = UnionFind(n)

    connections = 1000 if len(edges) >= 1000 else 10

    for k in range(connections):
        _, i, j = edges[k]
        uf.union(i, j)

    components = {}
    for i in range(n):
        root = uf.find(i)
        components[root] = components.get(root, 0) + 1

    sizes = sorted(components.values(), reverse=True)
    result = 1
    for s in sizes[:3]:
        result *= s
    return result


def part_2(filename):
    points = read_points(filename)
    edges = compute_edges(points)
    n = len(points)

    uf = UnionFind(n)
    total_components = n
    last_connection = None

    for _, i, j in edges:
        if uf.union(i, j):
            total_components -= 1
            last_connection = (i, j)
            if total_components == 1:
                break

    i, j = last_connection
    return points[i][0] * points[j][0]


print(f"Part 1: {part_1('data.txt')}")
print(f"Part 2: {part_2('data.txt')}")
