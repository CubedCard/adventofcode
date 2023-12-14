rock_grid = []

for line in open('data.txt'):
    rock_grid.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print(''.join(row))
    print()

def get_load():
    load = 0
    for i, row in enumerate(rock_grid):
        for item in row:
            if item == 'O':
                load += (len(rock_grid) - i)
    return load

def get_cols():
    cols = []
    for i in range(len(rock_grid[0])):
        cols.append([row[i] for row in rock_grid])
    return cols

def translate_cols_to_rows(cols):
    for i, row in enumerate(cols):
        for j, item in enumerate(row):
            rock_grid[j][i] = item

def roll_north(grid, row):
    index = grid.index(row)
    if index == 0:
        return grid
    for i, item in enumerate(row):
        if item == '#' or item == '.':
            continue
        else:
            if grid[index-1][i] == '.':
                grid[index-1][i] = 'O'
                grid[index][i] = '.'
    return roll_north(grid, grid[index-1])

def roll_south(grid, row):
    index = grid.index(row)
    if index == len(grid) - 1:
        return grid
    for i, item in enumerate(row):
        if item == '#' or item == '.':
            continue
        else:
            if grid[index+1][i] == '.':
                grid[index+1][i] = 'O'
                grid[index][i] = '.'
    return roll_south(grid, grid[index+1])

def roll_east(grid, col):
    return roll_south(grid, col)

def roll_west(grid, col):
    return roll_north(grid, col)

def do_cycle():
    # roll north
    for row in rock_grid:
        roll_north(rock_grid, row)

    # roll west
    cols = get_cols()
    for col in cols:
        roll_west(cols, col)

    translate_cols_to_rows(cols)

    # roll south
    for i in range(len(rock_grid)):
        roll_south(rock_grid, rock_grid[-1-i])

    # roll east
    cols = get_cols()
    for i in range(len(cols)):
        roll_east(cols, cols[-1-i])

    translate_cols_to_rows(cols)

for i in range(1000000000):
    if i % 1000 == 0:
        print(i, get_load())
    do_cycle()

print_grid(rock_grid)


print('Part 1:', get_load())

