data = []

for line in open('data.txt'):
    cords = []
    for cord in line.strip().split(','):
        cords.append(int(cord))
    data.append(cords)

total_sides = len(data) * 6

covered_sides = 0

# loop through the cubes to get the sides that are covered
for i in range(len(data)):
    for j in range(len(data)):
        difX = abs(data[i][0] - data[j][0])
        difY = abs(data[i][1] - data[j][1])
        difZ = abs(data[i][2] - data[j][2])
        adjacent_along_x = difX == 1 and difY == 0 and difZ == 0
        adjacent_along_y = difX == 0 and difY == 1 and difZ == 0
        adjacent_along_z = difX == 0 and difY == 0 and difZ == 1
        if (difX <= 1 and difY <= 1 and difZ <= 1) and (adjacent_along_x or adjacent_along_y or adjacent_along_z):
            covered_sides += 1

print(total_sides, covered_sides, total_sides - covered_sides)
