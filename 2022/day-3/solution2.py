lowercase = 96
uppercase = 38

array = []

priority_total = 0

for file in open('./data.txt'):
    line = file.strip()
    array.append(line)

for i in range(0, len(array), 3):
    first = array[i]
    second = array[i+1]
    third = array[i+2]
    for char in first:
        if char in second and char in third:
            if char.islower():
                priority_total += (ord(char) - lowercase)
            else:
                priority_total += (ord(char) - uppercase)
            break

print(priority_total)
