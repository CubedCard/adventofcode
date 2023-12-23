def get_bricks():
    bricks = []
    for line in open('data.txt'):
        xyzs = line.strip().split('~')
        xyz1 = xyzs[0].split(',')
        xyz2 = xyzs[1].split(',')
        bricks.append((xyz1, xyz2))

    bricks.sort(key=lambda x: min(int(x[0][2]), int(x[1][2])))
    return bricks

bricks = get_bricks()

def get_new_grid(b):
    new_grid = {}

    for i, brick in enumerate(b):
        x1, y1, z1 = brick[0]
        x2, y2, z2 = brick[1]
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2))+1):
            for y in range(min(int(y1), int(y2)), max(int(y1), int(y2))+1):
                for z in range(min(int(z1), int(z2)), max(int(z1), int(z2))+1):
                    new_grid[(x, y, z)] = chr(i+65)
    return new_grid

grid = get_new_grid(bricks)

def move_down(g, brick):
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    if int(z1) == 1:
        return False
    if z1 == z2:
        for x in range(int(x1), int(x2)+1):
            for y in range(int(y1), int(y2)+1):
                if (x, y, int(z1) - 1) in g and g[(x, y, int(z1)-1)] != '.':
                    return False
    else:
        min_z = min(int(z1), int(z2))
        for x in range(int(x1), int(x2)+1):
            for y in range(int(y1), int(y2)+1):
                if (x, y, min_z-1) in g and g[(x, y, min_z-1)] != '.':
                    return False
    return True

def move_bricks(g, b):
    for brick in b:
        can_move_down = move_down(g, brick)
        while can_move_down:
            x1, y1, z1 = brick[0].copy()
            x2, y2, z2 = brick[1].copy()
            letter = g[(int(x1), int(y1), int(z1))]
            if z1 == z2:
                for x in range(int(x1), int(x2)+1):
                    for y in range(int(y1), int(y2)+1):
                        g[(x, y, int(z1))] = '.' 
                        g[(x, y, int(z1)-1)] = letter
            else:
                min_z, max_z = min(int(z1), int(z2)), max(int(z1), int(z2))
                for x in range(int(x1), int(x2)+1):
                    for y in range(int(y1), int(y2)+1):
                        g[(x, y, max_z)] = '.'
                        g[(x, y, min_z-1)] = letter
            brick[0][2] = str(int(z1)-1)
            brick[1][2] = str(int(z2)-1)
            can_move_down = move_down(g, brick)
    return g

grid = move_bricks(grid, bricks)

def find_bricks():
    movable = {}
    for b, _ in enumerate(bricks):
        grid_copy = get_new_grid(bricks)
        char = chr(b+65)
        for xyz in grid_copy:
            if grid_copy[xyz] == char:
                grid_copy[xyz] = '.'
        movable[char] = not any([move_down(grid_copy, brick) for brick in bricks])
    return movable

def get_min_z(brick):
    x1, y1, z1 = brick[0]
    x2, y2, z2 = brick[1]
    return min(int(z1), int(z2))

def part2(movable):
    total_damage = 0
    for mov in movable:
        bricks_copy = get_bricks()
        grid_copy = get_new_grid(bricks_copy)
        grid_copy = move_bricks(grid_copy, bricks_copy)
        for xyz in grid_copy:
            if grid_copy[xyz] == mov:
                grid_copy[xyz] = '.'
        min_z_for_bricks = [get_min_z(brick) for brick in bricks_copy]
        move_bricks(grid_copy, bricks_copy)
        min_z_for_bricks_after = [get_min_z(brick) for brick in bricks_copy]
        for i, z in enumerate(min_z_for_bricks):
            if z != min_z_for_bricks_after[i]:
                total_damage += 1
        print(mov, total_damage)

    return total_damage


movable = find_bricks()
can_be_moved = len([x for x in movable if movable[x]])
most_damage = part2([x for x in movable if not movable[x]])
print(f"Part 1: {can_be_moved}")
print(f"Part 2: {most_damage}")
