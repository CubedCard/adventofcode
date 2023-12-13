grids = open('data.txt', 'r').read().split('\n\n')

for i in range(len(grids)):
    grids[i] = grids[i].strip().split('\n')

def print_grid(grid):
    for row in grid:
        print(row)

def get_rows_and_cols(grid):
    rows = grid[0:]
    cols = []
    for i in range(len(grid[0])):
        col = ''
        for row in rows:
            col += row[i]
        cols.append(col)
    return rows, cols

def valid_reflection(grid, index):
    errors = 0
    for i in range(len(grid)):
        try:
            if index - i < 0:
                break
            errors += sum([1 for j in range(len(grid[i])) if grid[index + 1 + i][j] != grid[index - i][j]])
        except IndexError:
            break
    return errors


def find_reflection(grid):
    rows, cols = get_rows_and_cols(grid)

    found_rows, found_cols = 0, 0
    for i in range(len(rows) - 1):
        if rows[i] == rows[i+1]:
            if valid_reflection(rows, i) == 0:
                found_rows = i + 1
    for i in range(len(cols) - 1):
        if cols[i] == cols[i+1]:
            if valid_reflection(cols, i) == 0:
                found_cols = i + 1
    return found_rows, found_cols

def find_smudge_reflections(grid):
    rows, cols = get_rows_and_cols(grid)

    found_rows, found_cols = 0, 0
    for i in range(len(rows) - 1):
        if valid_reflection(rows, i) == 1:
            found_rows = i + 1
            break
    for i in range(len(cols) - 1):
        if valid_reflection(cols, i) == 1:
            found_cols = i + 1
            break
    return found_rows, found_cols

number_of_rows, number_of_cols = 0, 0
number_of_smudge_rows, number_of_smudge_cols = 0, 0
for i, grid in enumerate(grids):
    rows, cols = find_reflection(grid)
    smudge_rows, smudge_cols = find_smudge_reflections(grid)

    number_of_rows += rows
    number_of_cols += cols
    number_of_smudge_rows += smudge_rows
    number_of_smudge_cols += smudge_cols

total = number_of_rows * 100 + number_of_cols
total_smudge = number_of_smudge_rows * 100 + number_of_smudge_cols

print(total)
print(total_smudge)
