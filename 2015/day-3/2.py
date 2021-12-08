from collections import defaultdict

houses = defaultdict(str)

for f in open('./text.txt'):
    up = '^'
    down = 'v'
    left = '<'
    right = '>'

    x_position = 0
    y_position = 0
    x_robo_position = 0
    y_robo_position = 0
    santa_turn = True

    for char in f:
        trimmed = char.strip()
        if trimmed == up:
            if santa_turn: y_position += 1
            else: y_robo_position += 1
        elif trimmed == down:
            if santa_turn: y_position -= 1
            else: y_robo_position -= 1 
        elif trimmed == left:
            if santa_turn: x_position -= 1
            else: x_robo_position -= 1
        elif trimmed == right:
            if santa_turn: x_position += 1
            else: x_robo_position += 1
        position = 0
        if santa_turn: position = str(x_position) + ',' + str(y_position)
        else: position = str(x_robo_position) + ',' + str(y_robo_position)
        if houses.get(position, -1) != -1:
            houses[position] += 1
        else: houses[position] = 1 
        santa_turn = not santa_turn

housesWithPresents = 0

for house in houses:
    if houses[house] > 0:
        housesWithPresents += 1

print(housesWithPresents)
