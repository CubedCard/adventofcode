grid = []

for line in open('data.txt'):
    grid.append(list(line.strip()))

def print_grid(grid):
    for row in grid:
        print("".join("■" if cell == 1 else "O" if cell == 8 else "." for cell in row))

def move_animal(row, col, direction):
    if direction == 'N':
        return row - 1, col
    elif direction == 'S':
        return row + 1, col
    elif direction == 'E':
        return row, col + 1
    elif direction == 'W':
        return row, col - 1
    else: 
        raise ValueError("Invalid direction")

def is_valid_move(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '.'

def find_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                return row, col
    raise ValueError("No start found")

def follow_pipes(grid):
    directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    start_row, start_col = find_start(grid)

    for direction in directions:
        # check if we can move in this direction
        row, col = move_animal(start_row, start_col, direction)
        if not is_valid_move(grid, row, col):
            continue

        current_direction = direction
        current_row, current_col = start_row, start_col

        path = []
        visited = set()
        while True:
            visited.add((current_row, current_col))
            path.append((current_row, current_col))

            current_tile = grid[current_row][current_col]

            if current_tile == "S" and len(path) > 1:
                return path
            if current_tile == ".":
                break


            if current_tile == '|':
                current_direction = 'S' if current_direction == 'S' else 'N'
            elif current_tile == '-':
                current_direction = 'W' if current_direction == 'W' else 'E'
            elif current_tile == 'L':
                current_direction = 'N' if current_direction == 'W' else 'E'
            elif current_tile == 'J':
                current_direction = 'N' if current_direction == 'E' else 'W'
            elif current_tile == '7':
                current_direction = 'S' if current_direction == 'E' else 'W'
            elif current_tile == 'F':
                current_direction = 'S' if current_direction == 'W' else 'E'
            
            current_row, current_col = move_animal(current_row, current_col, current_direction)

    return None


# Follow the pipes from 'S' to 'S'
path = follow_pipes(grid)

# Print the path
print("Path:")
if path: 
    for row, col in path:
        print(grid[row][col], end='')
    print()

    print("Final Grid:")
    for row, col in path:
        grid[row][col] = 1

    index = (len(path) - 1) / 2
    print("length: {}, Index: {}".format(len(path), int(index)))
    print_grid(grid)


