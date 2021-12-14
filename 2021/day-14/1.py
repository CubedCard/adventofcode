from collections import defaultdict

startLine = "BSONBHNSSCFPSFOPHKPK"
start = []

for char in startLine:
    start.append(char)

for line in open('./text.txt'):
    textLine = line.strip()
    pair, arrow, single = textLine.split(' ')

    step = start.copy()

    for pos in range(len(start) -1):
        if start[pos] == pair[0] and start[pos + 1] == pair[1]:
            step.insert(pos + 1, single)

    start = step.copy()

mapping = defaultdict(str)

for char in start:
    mapping[char] = mapping.get(char, 0) + 1

for mapp in mapping:
    print(mapping.get(mapp))
