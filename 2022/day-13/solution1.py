import read

pairs = read.get_list_of_lists('./data.txt')

index = 0
total = 0

for pair in pairs:
    index += 1
    pair1 = pair[0]
    pair2 = pair[1]
    if type(pair1) == type(pair2):
        if pair1 <= pair2:
            if len(pair1) > len(pair2):
                print('False')
            else:
                print('True', index)
                total += index
        else:
            print('False')
    elif type(pair1) == list or type(pair2) == list:
        list_ = []
        number = 0
        is_smaller = True
        if type(pair1) == list:
            list_ = pair1
            number = pair2
        else:
            list_ = pair2
            number = pair1
        for item in list_:
            if item > number:
                is_smaller = False
                break
        if is_smaller:
            if len(pair1) > len(pair2):
                print('False')
            else:
                print('True', index)
                total += index
        else:
            print('False')


print(total)
