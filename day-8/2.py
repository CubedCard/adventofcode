eight = '' 
zeven = ''
four = ''
one = ''
number = 0

for f in open('./text2.txt'):
    first, second = f.split("|")

    output2 = first.strip().split(" ")
    output = second.strip().split(" ")
    temp = "" 

    for combi in output2:
        length = len(combi)
        if length == 2: 
            one = combi 
        elif length == 3:
            seven = combi
        elif length == 4: 
            four = combi 
        elif length == 7:
            eight = combi


    for combi in output:
        length = len(combi)
        if length == 2: 
            temp += '1'
        elif length == 3:
            temp += '7'
        elif length == 4: 
            temp += '4'
        elif length == 7:
            temp += '8'
        elif eight[1] not in combi and eight[4] not in combi and length == 5:
            temp += '3'
        elif eight[2] not in combi and eight[4] not in combi and length == 5:
            temp += '5'
        elif eight[3] not in combi and length == 6:
            temp += '0'
        elif one[0] not in combi and length == 6:
            temp += '6'
        elif eight[4] not in combi and length == 6:
            temp += '9'

    #print(output2, output, temp)
    print(output, temp)
    if len(temp) > 0: number += int(temp.strip())


print(number)








