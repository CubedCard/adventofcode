space = []

for row in open('data.txt'):
    space.append(list(row.strip()))

# find the colums that don't contain a #
cols = []
for i in range(len(space[0])):
    for row in space:
        if row[i] == '#':
            break
    else:
        cols.append(i)

# change the space grid to double the cols that don't contain a #
for row in space:
    diff = 1
    for i in cols:
        row.insert(i + diff, '.')
        diff += 1

# rename the # to numbers in order of appearance
num = 1
for row in space:
    for i in range(len(row)):
        if row[i] == '#':
            row[i] = num
            num += 1

# find the shortest path between all the numbers in any order using JPS (Jump Point Search)
def shortest_path(start, end):
    open_list = [start]
    closed_list = []
    g = {start: 0}
    f = {start: 0}
    path = {}
    while open_list:
        current = min(open_list, key=lambda x: f[x])
        if current == end:
            data = []
            while current in path:
                data.append(current)
                current = path[current]
            return data[::-1]
        open_list.remove(current)
        closed_list.append(current)
        for neighbor in neighbors(current):
            if neighbor in closed_list:
                continue
            if neighbor not in open_list:
                open_list.append(neighbor)
            temp_g = g[current] + 1
            if neighbor in g and temp_g >= g[neighbor]:
                continue
            path[neighbor] = current
            g[neighbor] = temp_g
            f[neighbor] = temp_g + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])

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
        result = shortest_path(cords[i], cords[j])
        if result:
            total += len(result) + 1

print(total)
