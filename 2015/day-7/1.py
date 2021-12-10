from collections import defaultdict

values = defaultdict(str)

for file in open('./text.txt'):
    words = file.strip().split(' ')
    if words[0].isnumeric():
        print("nummer", words)

