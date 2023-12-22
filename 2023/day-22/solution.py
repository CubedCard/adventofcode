bricks = []

for line in open('ex.txt'):
    xyzs = line.strip().split('~')
    xyz1 = xyzs[0].split(',')
    xyz2 = xyzs[1].split(',')
    bricks.append((xyz1, xyz2))

grid = [[['.' for x in range(10)] for y in range(3)] for z in range(3)]

for i, brick in enumerate(bricks):
    for x in range(int(brick[0][0]), int(brick[1][0])+1):
        for y in range(int(brick[0][1]), int(brick[1][1])+1):
            for z in range(int(brick[0][2]), int(brick[1][2])+1):
                grid[x][y][z] = chr(i+65)

def print_grids():
    for x, _ in enumerate(grid):
        print("Layer", x)
        for y, _ in enumerate(grid[x]):
            for z, _ in enumerate(grid[x][y]):
                print(grid[x][y][z], end='')
            print()
        print()

print_grids()

def move_down(brick):
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    if int(z1) == 1:
        return False
    for x in range(int(x1), int(x2)+1):
        for y in range(int(y1), int(y2)+1):
            if grid[x][y][int(z1)-1] != '.':
                return False
    return True

for brick in bricks:
    can_move_down = move_down(brick)
    while can_move_down:
        x1, y1, z1 = brick[0]
        x2, y2, z2 = brick[1]
        letter = grid[int(x1)][int(y1)][int(z1)]
        for x in range(int(x1), int(x2)+1):
            for y in range(int(y1), int(y2)+1):
                grid[x][y][int(z1)+1] = '.'
                grid[x][y][int(z1)] = letter
        brick[0][2] = str(int(z1)-1)
        brick[1][2] = str(int(z2)-1)
        can_move_down = move_down(brick)

print_grids()
