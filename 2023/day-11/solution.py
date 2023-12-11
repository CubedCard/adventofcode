# to low:  9501638
# to high: 9792001
# answer:  9769724

space = []

for row in open('data.txt'):
    space.append(list(row.strip()))

# find the rows and colums that don't contain a #
cols = []
for i in range(len(space[0])):
    for row in space:
        if row[i] == '#':
            break
    else:
        cols.append(i)

rows = []
for i, row in enumerate(space):
    if '#' not in row:
        rows.append(i)

# change the space grid to double the cols that don't contain a #
for row in space:
    diff = 1
    for i in cols:
        row.insert(i + diff, '.')
        diff += 1

# change the space grid to double the rows that don't contain a #
row_diff = 1
for row in rows:
    space.insert(row + row_diff, ['.'] * len(space[0]))

for row in space:
    print(row)

# rename the # to numbers in order of appearance
num = 1
for row in space:
    for i in range(len(row)):
        if row[i] == '#':
            row[i] = num
            num += 1

# find the shortest path between all the numbers in any order using BFS, and add the distance to a dictionary
from collections import deque

def bfs(start, end):
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return None

def neighbors(node):
    rows, cols = len(space), len(space[0])
    x, y = node
    neighbors = []
    for i, j in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
        if 0 <= i < rows and 0 <= j < cols and space[i][j] != '#':
            neighbors.append((i, j))
    return neighbors


# get the cords of all the numbers
cords = {}
for row in range(len(space)):
    for col in range(len(space[0])):
        if str(space[row][col]).isdigit():
            cords[space[row][col]] = (row, col)


# do it between all the numbers and get the sum
total = 0
for i in range(1, len(cords) + 1):
    for j in range(i + 1, len(cords) + 1):
        result = bfs(cords[i], cords[j])
        print(f'{i} -> {j} = {result}')
        if result:
            total += result

print(total)
