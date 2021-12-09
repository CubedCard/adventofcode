import hashlib

file_input = 'yzbqklnj'
found = False
number = 0

while found == False:
    string = file_input + str(number)
    the_hash = (hashlib.md5(string.encode()))
    number += 1

    hexi = the_hash.hexdigest()

    good = True
    for x in range(6): # or 5 for part 1
        if hexi[x] != '0':
            good = False

    if good:
        print(string)

    found = good

print(the_hash.hexdigest())
