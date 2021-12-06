dot = 0 

rows, cols = (1000, 1000)
grid = [[dot for i in range(cols)] for j in range(rows)]

def printGrid():
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) 
        for row in grid]))

text = "" 

number = 0

for f in open('./text.txt'):
    first, second = f.split("->")

    x1, y1 = first.split(",")
    x2, y2 = second.split(",")

    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())

    if x1 == x2:
        for y in range(y1, y2 + 1):
            grid[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            grid[y1][x] += 1

for row in grid:
    for item in row:
        if item >= 2:
            number += 1

#printGrid()
print(number)
