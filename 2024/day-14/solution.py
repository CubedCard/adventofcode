import re

width, height = 101, 103

data = [
    list(map(int, re.findall(r"-?\d+", line)))
    for line in open("data.txt")
]

def compute_danger(t):
    quadrants = [0, 0, 0, 0]

    for x, y, dx, dy in data:
        x = (x + dx * t) % width
        y = (y + dy * t) % height

        if x > width // 2 and y > height // 2:
            quadrants[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrants[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

    return quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

print(f"Part 1: {compute_danger(100)}")
print(f"Part 2: {min(range(10**4), key=compute_danger)}")