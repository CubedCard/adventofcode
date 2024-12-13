import numpy as np
import re

def solve(part_2=0):
    tokens = 0
    for a, b, p in matches:
        ax, ay, px = a[0], b[0], p[0] + part_2
        bx, by, py = a[1], b[1], p[1] + part_2
        x, y = np.linalg.solve(np.array([[ax, ay], [bx, by]]), np.array([px, py]))
        if round(x, 2).is_integer() and round(y, 2).is_integer():
            tokens += int(round(x, 0) * 3 + round(y, 0))
    return tokens

def get_matches(pattern, text):
    matches = re.findall(pattern, text)
    return [
        [
            (int(match[0]), int(match[1])),
            (int(match[2]), int(match[3])),
            (int(match[4]), int(match[5])),
        ]
        for match in matches
    ]

pattern = r"Button A: X\+(\d+), Y\+(\d+)\s+Button B: X\+(\d+), Y\+(\d+)\s+Prize: X=(\d+), Y=(\d+)"
matches = get_matches(pattern, open('data.txt').read())

part_1 = solve()
part_2 = solve(10**13)

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

assert part_1 == 29598                                                                                                                                                                                                              
assert part_2 == 93217456941970