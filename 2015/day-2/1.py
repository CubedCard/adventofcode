total = 0

for f in open('./text.txt'):
    text = f.strip().split('\n')

    for row in text:
        numbers = row.split('x')
        l = int(numbers[0])
        w = int(numbers[1])
        h = int(numbers[2])

        side_1 = l*w
        side_2 = w*h
        side_3 = h*l

        smallest_side = min(side_1, side_2, side_3)

        surface_area = 2*side_1 + 2*side_2 + 2*side_3 + smallest_side
        print(l,w,h, surface_area)
        total += surface_area
print(total)
