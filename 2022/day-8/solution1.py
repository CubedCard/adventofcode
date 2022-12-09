data = dict()

i = 0
for line in open('./data.txt'):
    data[i] = line.strip()
    i += 1

visible = 0

for key in data:
    for index in range(len(data[key])):
        if key == 0:
            visible += 1
            continue
        elif key == len(data) - 1:
            visible += 1
            continue
        else:
            if index == 0:
                visible += 1
                continue
            elif index == len(data[key]) - 1:
                visible += 1
                continue
            top = True
            bottom = True
            left = True
            right = True
            for i in range(0, key):
                if data[i][index] >= data[key][index]:
                    top = False
                    break
            for i in range(key + 1, len(data)):
                if data[i][index] >= data[key][index]:
                    bottom = False
                    break
            for i in range(0, index):
                if data[key][i] >= data[key][index]:
                    left = False
                    break
            for i in range(index + 1, len(data[key])):
                if data[key][i] >= data[key][index]:
                    right = False
                    break
            if top or bottom or left or right:
                visible += 1

print(visible)
