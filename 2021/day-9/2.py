array = []

for file in open('./text3.txt'):
    line = file.strip()
    array.append(line)

def recurseFind(x, y, count):
    current = int(array[x][y])
    if current != 9:
        count += 1
    if x < len(array) - 1 and y < len(array[x]) - 1:
        return recurseFind(x + 1, y, count) + recurseFind(x, y + 1, count)
    else:
        return count

print(recurseFind(0,0,0))
