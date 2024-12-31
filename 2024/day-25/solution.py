def get_heights(schematic, is_lock=True):
    num_columns = len(schematic[0])
    row_range = range(len(schematic)) if is_lock else range(len(schematic)-1, -1, -1)
    
    return [sum(1 for row in row_range if schematic[row][col] == '#') for col in range(num_columns)]

def find_compatible_locks_and_keys(lock_heights, key_heights, max_height=7):
    return [
        (lock_index + 1, key_index + 1)
        for lock_index, lock in enumerate(lock_heights)
        for key_index, key in enumerate(key_heights)
        if all(lock[col] + key[col] <= max_height for col in range(len(lock)))
    ]

def part_1(file="data.txt"):
    sections = open(file).read().strip().split('\n\n')
    lock_schematics, key_schematics = [], []

    for section in sections:
        lines = section.split('\n')
        is_key = lines[-1].count('#') == len(lines[-1])
        
        (key_schematics if is_key else lock_schematics).append(lines)

    lock_heights = [get_heights(lock, is_lock=True) for lock in lock_schematics]
    key_heights = [get_heights(key, is_lock=False) for key in key_schematics]


    return len(find_compatible_locks_and_keys(lock_heights, key_heights))

print(f"Part 1: {part_1()}")
assert part_1('ex.txt') == 3
assert part_1() == 3291 