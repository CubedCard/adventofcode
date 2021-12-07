dot = 0 

rows, cols = (1000, 1000)
grid = [[dot for i in range(cols)] for j in range(rows)]

number = 0

for f in open('./text.txt'):
    first, second = f.split("->")

    x1, y1 = first.split(",")
    x2, y2 = second.split(",")

    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())

    xstart = x1
    ystart = y1

    xValue = 1
    yValue = 1

    if x1 > x2:
        xValue = -1
    if y1 > y2:
        yValue = -1
        

    x1,x2 = min(x1, x2), max(x1,x2)
    y1,y2 = min(y1, y2), max(y1,y2)
    xDif = x2 - x1
    yDif = y2 - y1

    if x1 == x2:
        for y in range(y1, y2 + 1):
            grid[y][x1] += 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            grid[y1][x] += 1
    elif xDif == yDif:
        for x in range(xDif + 1):
            grid[ystart][xstart] += 1
            xstart = xstart + xValue
            ystart = ystart + yValue



# count the number of elements with a value of 2 or higher
for row in grid:
    for item in row:
        if item >= 2:
            number += 1

#for row in grid:
#    for val in row:
#        if val != 0: print(val),
#        else: print("."),
#    print

print(number)
