def find_guard_pos(grid):
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == "^":
                return row, col
    return None

def is_within_bounds(row, col, height, width):
    return 0 <= row < height and 0 <= col < width

def simulate_patrol(grid, start_row, start_col, target_row=None, target_col=None):
    height = len(grid)
    width = len(grid[0])
    visited = set()
    row, col = start_row, start_col
    direction = (-1, 0)  

    while True:
        if not is_within_bounds(row, col, height, width):
            return len(visited) if target_row is None else False

        if grid[row][col] == "#" or (row == target_row and col == target_col):
            row -= direction[0]
            col -= direction[1]
            direction = (direction[1], -direction[0])  

        elif (row, col, direction) in visited:
            return True

        else:
            if target_row is None:
                visited.add((row, col))
            else:
                visited.add((row, col, direction))

            row += direction[0]
            col += direction[1]

def part_one(grid, guard_pos):
    return simulate_patrol(grid, guard_pos[0], guard_pos[1])

def part_two(grid):
    height = len(grid)
    width = len(grid[0])
    loop_count = 0

    for row in range(height):
        for col in range(width):
            if grid[row][col] == ".":  
                if simulate_patrol(grid, guard_pos[0], guard_pos[1], row, col):
                    loop_count += 1

    return loop_count

if __name__ == "__main__":
    grid = open("data.txt").read().splitlines()

    guard_pos = find_guard_pos(grid)

    print(f"Part 1: {part_one(grid, guard_pos)}")
    print(f"Part 2: {part_two(grid)}")