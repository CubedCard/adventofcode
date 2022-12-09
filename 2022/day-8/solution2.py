data = dict()

i = 0
for line in open('./data.txt'):
    data[i] = line.strip()
    i += 1

visible = 0

for key in data:
    for index in range(len(data[key])):
        top = 0
        bottom = 0
        left = 0
        right = 0
        for i in reversed(range(0, key)):
            top += 1
            if data[i][index] >= data[key][index]:
                break
        for i in range(key + 1, len(data)):
            bottom += 1
            if data[i][index] >= data[key][index]:
                break
        for i in reversed(range(0, index)):
            left += 1
            if data[key][i] >= data[key][index]:
                break
        for i in range(index + 1, len(data[key])):
            right += 1
            if data[key][i] >= data[key][index]:
                break
        visible = max(visible, top * bottom * left * right)

print(visible)
