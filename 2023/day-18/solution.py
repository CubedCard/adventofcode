instructions = []
colors = []

for line in open('data.txt'):
    instruction, value, color = line.strip().split(' ')
    instructions.append((instruction, int(value)))
    colors.append(color)

def get_path_part1(instructions):
    x, y = 0, 0
    path = [(x, y)]

    for direction, steps in instructions:
        if direction == 'R':
            x += steps
        elif direction == 'L':
            x -= steps
        elif direction == 'U':
            y += steps
        elif direction == 'D':
            y -= steps
        path.append((x, y))

    return path

def get_path_length(instructions):
    length = 0
    for _, steps in instructions:
        length += steps
    return length



def get_instructions_part2():
    new_instructions = []
    for color in colors:
        dir_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
        direction = dir_map[color[-2]]
        hex_value = int(color[2:-2], 16)
        new_instructions.append((direction, hex_value))
    return new_instructions


def shoelace_formula(x, y):
    n = len(x)
    area = 0.5 * abs(sum(x[i] * y[(i + 1) % n] - x[(i + 1) % n] * y[i] for i in range(n)))
    return area

def calculate_surface_area(outline):
    x_coordinates, y_coordinates = zip(*outline)
    surface_area = shoelace_formula(x_coordinates, y_coordinates)
    return surface_area

def part1(path, length):
    area = calculate_surface_area(path)
    total = int(area + 1 - length / 2 + length)
    return total

def part2():
    instructions = get_instructions_part2()
    path = get_path_part1(instructions)
    length = get_path_length(instructions)
    return part1(path, length)


print('Part 1:', part1(get_path_part1(instructions), get_path_length(instructions)))
print('Part 2:', part2())
