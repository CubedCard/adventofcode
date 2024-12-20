import re

data = open('data.txt').read()

grid_size = 1000
grid = [[[] for _ in range(grid_size)] for _ in range(grid_size)]

regex = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"
matches = re.findall(regex, data)

for match in matches:
    n, x, y, w, h = [int(k) for k in match]
    for i in range(w):
        for j in range(h):
            grid[x + i][y + j].append(n)

def part_1(): 
    return len([1 for i in range(grid_size) for j in range(grid_size) if len(grid[i][j]) > 1])

def part_2():
    dubs = [num for i in range(grid_size) for j in range(grid_size) if len(grid[i][j]) > 1 for num in grid[i][j]]
    for x in range(1, 1349):
        if x not in dubs:
            return x

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
