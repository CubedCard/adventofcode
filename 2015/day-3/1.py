from collections import defaultdict

houses = defaultdict(str)

for f in open('./text.txt'):
    up = '^'
    down = 'v'
    left = '<'
    right = '>'

    x_position = 0
    y_position = 0

    for char in f:
        trimmed = char.strip()
        if trimmed == up:
            y_position += 1
        elif trimmed == down:
            y_position -= 1
        elif trimmed == left:
            x_position -= 1
        elif trimmed == right:
            x_position += 1
        position = str(x_position) + ',' + str(y_position)
        if houses.get(position, -1) != -1:
            houses[position] += 1
        else: houses[position] = 1 

housesWithPresents = 0

for house in houses:
    if houses[house] > 0:
        housesWithPresents += 1

print(housesWithPresents)
