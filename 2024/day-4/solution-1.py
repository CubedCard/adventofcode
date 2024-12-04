import re 

grid = [line.strip() for line in open('data.txt')]

def get_vertical_strings(grid):
    return [''.join(grid[row][col] for row in range(len(grid))) for col in range(len(grid[0]))]

def get_horizontal_strings(grid):
    return grid

def get_diagonal_strings(grid):
    diagonals = []

    for col in range(len(grid[0])):
        diagonal = []
        x, y = 0, col
        while x < len(grid) and y < len(grid[0]):
            diagonal.append(grid[x][y])
            x += 1
            y += 1
        diagonals.append(''.join(diagonal))

    for row in range(1, len(grid)):
        diagonal = []
        x, y = row, 0
        while x < len(grid) and y < len(grid[0]):
            diagonal.append(grid[x][y])
            x += 1
            y += 1
        diagonals.append(''.join(diagonal))

    for col in range(len(grid[0])):
        diagonal = []
        x, y = 0, col
        while x < len(grid) and y >= 0:
            diagonal.append(grid[x][y])
            x += 1
            y -= 1
        diagonals.append(''.join(diagonal))

    for row in range(1, len(grid)):
        diagonal = []
        x, y = row, len(grid[0]) - 1
        while x < len(grid) and y >= 0:
            diagonal.append(grid[x][y])
            x += 1
            y -= 1
        diagonals.append(''.join(diagonal))

    return diagonals

vertical_strings = get_vertical_strings(grid)
horizontal_strings = get_horizontal_strings(grid)
diagonal_strings = get_diagonal_strings(grid)

def part_1():
    total = 0

    def getMatchesFor(strings):
        pattern = r"XMAS"
        total = 0
        for string in strings:
            matches = re.findall(pattern, string)
            reverse_matches = re.findall(pattern, string[::-1])
            total += len(matches) + len(reverse_matches)
        return total

    total += getMatchesFor(vertical_strings)
    total += getMatchesFor(horizontal_strings)
    total += getMatchesFor(diagonal_strings)

    return total

print(f"Part 1: {part_1()}")
