from collections import defaultdict

startLine = "BSONBHNSSCFPSFOPHKPK"
start = []
rules = defaultdict(str)

for char in startLine:
    start.append(char)

for line in open('./text.txt'):
    textLine = line.strip()
    pair, arrow, single = textLine.split(' ')

    rules[pair] = single

for x in range(10):
    for pos in range(len(start) - 1):
        if start[pos] + start[pos + 1] in rules:
            #print(start[pos] + start[pos + 1], rules[start[pos] + start[pos + 1]])
            start.insert(pos + 1, rules[start[pos] + start[pos + 1]])
            #print(start)

mapping = defaultdict(str)

for char in start:
    mapping[char] = mapping.get(char, 0) + 1

for mapp in mapping:
    print(mapping.get(mapp))
