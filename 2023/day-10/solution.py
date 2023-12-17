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
                if current_direction == 'N' or current_direction == 'S':
                    current_direction = 'S' if current_direction == 'S' else 'N'
                else: 
                    break
            elif current_tile == '-':
                if current_direction == 'E' or current_direction == 'W':
                    current_direction = 'W' if current_direction == 'W' else 'E'
                else:
                    break
            elif current_tile == 'L':
                if current_direction == 'W' or current_direction == 'S':
                    current_direction = 'N' if current_direction == 'W' else 'E'
                else:
                    break
            elif current_tile == 'J':
                if current_direction == 'E' or current_direction == 'S':
                    current_direction = 'N' if current_direction == 'E' else 'W'
                else:
                    break
            elif current_tile == '7':
                if current_direction == 'N' or current_direction == 'E':
                    current_direction = 'S' if current_direction == 'E' else 'W'
                else:
                    break
            elif current_tile == 'F':
                if current_direction == 'N' or current_direction == 'W':
                    current_direction = 'S' if current_direction == 'W' else 'E'
                else:
                    break

            current_row, current_col = move_animal(current_row, current_col, current_direction)

    return None


path = follow_pipes(grid)

if path: 
    index = (len(path) - 1) / 2
    print('Part 1: length: {}, Index: {}'.format(len(path), int(index)))
    
    outside_of_path = set()

    for i, line in enumerate(grid):
        inside_of_path = False
        up = None
        for j, char in enumerate(line):
            char = str(char)
            if (i, j) in path:
                if char in "LF":
                    up = char == "L"
                elif char == "|":
                    inside_of_path = not inside_of_path
                elif char in "7J":
                    if char != ("J" if up else "7"):
                        inside_of_path = not inside_of_path
                    up = None

            if not inside_of_path:
                outside_of_path.add((i, j))

    print('Part 2:', len(grid) * len(grid[0]) - len(outside_of_path | set(path)))
