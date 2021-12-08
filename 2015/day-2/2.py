total = 0

for f in open('./text.txt'):
    text = f.strip().split('\n')

    for row in text:
        numbers = row.split('x')
        l = int(numbers[0])
        w = int(numbers[1])
        h = int(numbers[2])

        largest_side = max(l, w, h)

        numbers.remove(str(largest_side))

        ribbon_area = 0

        for number in numbers:
            ribbon_area += 2*int(number)

        ribbon_area += l*w*h

        total += ribbon_area 
print(total)
