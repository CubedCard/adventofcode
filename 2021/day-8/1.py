number = 0

for f in open('./text.txt'):
    first, second = f.split("|")

    output = second.strip().split(" ")

    for combi in output:
        length = len(combi)
        if length  == 2 or length == 3 or length == 4 or length == 7:
            number += 1
            print(combi)

print(number)
