for text in open('./text.txt'):
    #print(text)
    up = '('
    down = ')'

    current_floor = 0

    for char in text:
        if char == up:
            current_floor += 1
        elif char == down:
            current_floor -= 1

    print(current_floor)
