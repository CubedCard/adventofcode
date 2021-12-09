combi = {'ab','cd','pq','xy'}

vowels = 'aeiou'

nice = 0

def lineIsNice(line):
    numberOfVowels = 0
    for vowel in vowels:
        numberOfVowels += line.count(vowel)
    if numberOfVowels < 3:
        return False

    numberOfDublicates = 0
    for x in range(len(line) - 1):
        if line[x] == line[x + 1]:
            numberOfDublicates += 1
    if numberOfDublicates == 0:
        return False

    for combination in combi:
        if combination in line:
            return False

    return True

for f in open('./text.txt'):
    stripped = f.strip()

    if lineIsNice(stripped):
        nice += 1

print(nice)
