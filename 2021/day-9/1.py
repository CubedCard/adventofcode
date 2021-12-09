array = []

for file in open('./text.txt'):
    line = file.strip()
    array.append(line)

number = 0

for x in range(len(array)):
    for y in range(len(array[x])):
        current = int(array[x][y])
        if y == 0 or current < int(array[x][y - 1]):
            if x == 0 or current < int(array[x - 1][y]):
                if x == (len(array) - 1) or current < int(array[x + 1][y]):
                    if y == (len(array[x]) - 1) or current < int(array[x][y + 1]):
                        number += current + 1


print(number)
