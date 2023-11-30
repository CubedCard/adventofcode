chars = [
        ')',
        ']',
        '}',
        '>',
        '(',
        '[',
        '{',
        '<'
        ]

points = [3, 57, 1197, 25137]

def checkIfCorrupted(line):
    print(line)
    scores = [0,0,0,0,0,0,0,0]

    for char in line:
        for ch in chars:
            if char == ch:
                if chars.index(char) < 4:
                    scores[chars.index(char)] -= 1
                else:
                    scores[chars.index(char)] += 1

                if scores[chars.index(char)] < 0:
                    print(char)
                    return points[chars.index(ch)]

number = 0

for f in open('./text3.txt'):
    text = f.strip()
    number += checkIfCorrupted(text)

print(number)
