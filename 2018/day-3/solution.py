import re

grid_size = 1000
grid = [[[] for _ in range(grid_size)] for _ in range(grid_size)]

matches = re.findall(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", open('data.txt').read())

for match in matches:
    n, x, y, w, h = [int(k) for k in match]
    [grid[x + i][y + j].append(n) for i in range(w) for j in range(h)]

def part_1(): 
    return len([1 for i in range(grid_size) for j in range(grid_size) if len(grid[i][j]) > 1])

def part_2():
    dubs = [num for i in range(grid_size) for j in range(grid_size) if len(grid[i][j]) > 1 for num in grid[i][j]]
    return [x for x in range(1, len(matches)) if x not in dubs][0]

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")