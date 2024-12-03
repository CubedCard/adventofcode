import re

def part_1(file):
    input_string = open(f'{file}.txt').readline()
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input_string)
    return sum(int(a) * int(b) for a, b in matches)

def part_2(file):
    input_string = open(f'{file}.txt').readline()

    pattern = r"(mul\((\d{1,3}),(\d{1,3}\))|do\(\)|don't\(\))"

    matches = re.findall(pattern, input_string)

    result = 0
    active = True
    for match in matches:
        if "mul" in match[0] and active:
            result += int(match[1]) * int(match[2][:-1])
        elif match[0] == "do()":
            active = True
        else:
            active = False 

    return result

print(f'Part 1: {part_1("data")}')
print(f'Example Part 1: {part_1("ex")}')

assert part_1("data") == 188116424
assert part_1("ex") == 161

print(f'Part 2: {part_2("data")}')
print(f'Example Part 2: {part_2("ex")}')

assert part_2("data") == 104245808
assert part_2("ex") == 48
