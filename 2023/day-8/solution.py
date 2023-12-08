from itertools import cycle
import re

data = open('data.txt', 'r').read().split('\n\n')

instructions = [x for x in data[0]]

lines = data[1].split('\n')
roadmap = {}

for line in lines:
    match = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
    if match:
        start, left, right = match.group(1), match.group(2), match.group(3)
        roadmap[start] = (left, right)
    else:
        print("No match")

def lcm_of_steps(steps):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x * y // gcd(x, y)

    if len(steps) == 0:
        return None

    result = steps[0]
    for num in steps[1:]:
        result = lcm(result, num)

    return result

def part1():
    current = 'AAA'
    steps = 0

    for instruction in cycle(instructions):
        steps += 1
        current = roadmap[current][0] if instruction == 'L' else roadmap[current][1]
        if current == 'ZZZ':
            break

    return steps

def part2():
    currents = [current for current in roadmap.keys() if current.endswith('A')]

    steps_for_currents = [0] * len(currents)
    for i, node in enumerate(currents):
        for instruction in cycle(instructions):
            steps_for_currents[i] += 1
            node = roadmap[node][0] if instruction == 'L' else roadmap[node][1]
            if node.endswith('Z'):
                break

    return lcm_of_steps(steps_for_currents)

print(part1())
print(part2())
