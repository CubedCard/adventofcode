import re 

schematic = []

for line in open('data.txt'):
    schematic.append(line.strip())

neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
non_symbols = set('0123456789.\n')

def is_symbol(row, col):
    return row >= 0 and row < len(schematic) and col >= 0 and col < len(schematic[0]) and schematic[row][col] not in non_symbols

def is_digit(row, col):
    return row >= 0 and row < len(schematic) and col >= 0 and col < len(schematic[0]) and schematic[row][col].isdigit()

def get_adjacent_digits(grid, row, col):
    current_digit = grid[row][col]
    neighbors = [current_digit]
    
    # Check left neighbors
    for c in range(col - 1, -1, -1):
        if grid[row][c].isdigit():
            neighbors.insert(0, grid[row][c])  # Insert at the beginning to maintain order
        else:
            break  # Stop if we encounter a non-digit character
    
    # Check right neighbors
    for c in range(col + 1, len(grid[row])):
        if grid[row][c].isdigit():
            neighbors.append(grid[row][c])
        else:
            break  # Stop if we encounter a non-digit character
    
    return ''.join(neighbors)

def part1():
    total = 0
    for i, line in enumerate(schematic):
        indexes = re.finditer(r"\d+", line)
        for x in indexes:
            first_index = x.start()
            last_index = x.end() - 1

            parts = []
            for neighbour_row, neighbour_col in neighbours:
                new_row = i + neighbour_row
                parts.append(is_symbol(new_row, first_index + neighbour_col))
                parts.append(is_symbol(new_row, last_index + neighbour_col))

            if any(parts):
                total += int(x.group())

    return total

def part2():
    total = 0
    for i, line in enumerate(schematic):
        asterisks = re.finditer(r"\*", line)
        for x in asterisks:
            first_index = x.start()
            last_index = x.end() - 1

            parts = set()
            for neighbour_row, neighbour_col in neighbours:
                new_row = i + neighbour_row
                if is_digit(new_row, first_index + neighbour_col):
                    parts.add(int(get_adjacent_digits(schematic, new_row, first_index + neighbour_col)))
                if is_digit(new_row, last_index + neighbour_col):
                    parts.add(int(get_adjacent_digits(schematic, new_row, last_index + neighbour_col)))

            print(parts)
            if len(parts) == 2:
                total += parts.pop() * parts.pop()

    return total

print(part1())
print(part2())

