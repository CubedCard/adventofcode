for text in open('./text.txt'):
    #print(text)
    up = '('
    down = ')'

    current_floor = 0
    position = 0

    for char in text:
        position += 1
        if char == up:
            current_floor += 1
        elif char == down:
            current_floor -= 1
        if current_floor == -1:
            print(position)
            exit()


    print(current_floor)
