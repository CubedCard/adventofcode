nice = 0

def lineIsNice(line):
    pairs = []
    for x in range(len(line) - 1):
        if line.count(line[x] + line[x + 1]) > 1:
            pairs.append(line[x] + line[x + 1])

    twoPairs = False
    for pair in pairs:
        timesInLine = line.count(pair)
        if timesInLine > 1:
            twoPairs = True

    if twoPairs == False:
        return False 
    
    for x in range(len(line) - 2):
        if line[x] == line[x + 2]:
            return True
    
    return False

for f in open('./text.txt'):
    stripped = f.strip()

    if lineIsNice(stripped):
        nice += 1

print(nice)
