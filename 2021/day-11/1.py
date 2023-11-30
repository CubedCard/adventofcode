octos = []
shine = [0]


def increase(x, y, num):
    octo = octos[x][y]
    octo = octo + num
    if octo == 9:
        shine[0] += 1
        if x > 0:
            increase(x - 1, y, num)
        if y > 0:
            increase(x, y - 1, num)
        if y < len(octos[x]) - 1:
            increase(x, y + 1, num)
        if x < len(octos) - 1:
            increase(x + 1, y, num)


# put all octo integers in the octos array
for octi in open('./text.txt'):
    line = octi.strip()

    octoLine = []
    for octo in line:
        octoLine.append(int(octo))

    octos.append(octoLine)

for i in range(100):
    for x in range(len(octos)):
        for y in range(len(octos[x])):
            increase(x, y, 1)

print(octos)
print(shine)
