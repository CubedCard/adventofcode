from functools import cache

keypad_coordinates = { '7': 0, '8': 1, '9': 2, '4': 1j, '5': 1 + 1j, '6': 2 + 1j, '1': 2j, '2': 1 + 2j, '3': 2 + 2j, ' ': 3j, '0': 1 + 3j, 'A': 2 + 3j }
directional_coordinates = { ' ': 0, '^': 1, 'A': 2, '<': 1j, 'v': 1 + 1j, '>': 2 + 1j }

@cache
def calculate_path(start_key, end_key):
    coordinates = keypad_coordinates if start_key in keypad_coordinates and end_key in keypad_coordinates else directional_coordinates
    difference = coordinates[end_key] - coordinates[start_key]
    horizontal_steps, vertical_steps = int(difference.real), int(difference.imag)

    vertical_directions = ("^" * -vertical_steps) + ("v" * vertical_steps)
    horizontal_directions = ("<" * -horizontal_steps) + (">" * horizontal_steps)

    empty_space_difference = coordinates[' '] - coordinates[start_key]
    prefer_vertical_first = (horizontal_steps > 0 or empty_space_difference == horizontal_steps) and empty_space_difference != vertical_steps * 1j

    return (vertical_directions + horizontal_directions if prefer_vertical_first else horizontal_directions + vertical_directions) + "A"

@cache
def calculate_code_length(code_sequence, recursion_depth):
    return len(code_sequence) if recursion_depth == 0 else sum(calculate_code_length(calculate_path(code_sequence[i - 1], current_char), recursion_depth - 1) for i, current_char in enumerate(code_sequence))

if __name__ == "__main__":
    codes = open('data.txt').read().split()

    print(f"Part 1: {sum(int(code[:-1]) * calculate_code_length(code, 3) for code in codes)}")
    print(f"Part 2: {sum(int(code[:-1]) * calculate_code_length(code, 26) for code in codes)}")