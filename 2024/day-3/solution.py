import re

def part_1(file):
    input_string = open(f'{file}.txt').readline()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_string)
    return sum(int(a) * int(b) for a, b in matches)

def part_2(file):
    input_string = open(f'{file}.txt').readline()

    pattern, pattern_do, pattern_dont = r"mul\(\d{1,3},\d{1,3}\)", r"do\(\)", r"don't\(\)"

    matches = re.findall(pattern, input_string)
    matches_do = [m.start(0) for m in re.finditer(pattern_do, input_string)]
    matches_dont = [m.start(0) for m in re.finditer(pattern_dont, input_string)]

    valid_indexes = []

    active = True

    for i in range(len(input_string)):
        if i in matches_do:
            active = True
        elif i in matches_dont:
            active = False

        if active:
            valid_indexes.append(i)

    valid_matches = [match for match in matches if input_string.find(match) in valid_indexes]

    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    return sum([sum(int(a) * int(b) for a, b in re.findall(mul_pattern, match)) for match in valid_matches])


print(f'Part 1: {part_1("data")}')
print(f'Example Part 1: {part_1("ex")}')

assert part_1("data") == 188116424
assert part_1("ex") == 161

print(f'Part 2: {part_2("data")}')
print(f'Example Part 2: {part_2("ex")}')

assert part_2("data") == 104245808
assert part_2("ex") == 48