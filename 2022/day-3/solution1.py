lowercase = 96
uppercase = 38

array = []

priority_total = 0

for file in open('./data.txt'):
    line = file.strip()
    array.append(line)

for line in array:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    for char in first:
        if char in second:
            if char.islower():
                priority_total += (ord(char) - lowercase)
            else:
                priority_total += (ord(char) - uppercase)
            break

print(priority_total)
