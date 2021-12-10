dot = 0 

rows, cols = (1001, 1001)
grid = [[dot for i in range(cols)] for j in range(rows)]

def toggle(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if grid[x][y] == 0:
                grid[x][y] = 1
            else:
                grid[x][y] = 0

def off(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = 0

def on(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = 1

for line in open('./text.txt'):
    text = line.strip()

    content = text.split(' ')

    if len(content) == 4:
        x1, y1 = content[1].split(',')
        x2, y2 = content[3].split(',')
        toggle(int(x1), int(y1), int(x2), int(y2))
    else:
        x1, y1 = content[2].split(',')
        x2, y2 = content[4].split(',')
        if content[1] == "on":
            on(int(x1), int(y1), int(x2), int(y2))
        if content[1] == "off":
            off(int(x1), int(y1), int(x2), int(y2))

number = 0

for line in grid:
    for item in line:
        if item == 1:
            number += 1

print(number)
