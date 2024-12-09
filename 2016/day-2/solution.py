data = open('data.txt').read().strip().split('\n')

def get_code(keys, pos):
    code = []
    for ins in data:
        x, y = pos
        for i in ins:
            if i == 'U':
                if [x, y - 1] in keys.values():
                    y -= 1
            if i == 'D':
                if [x, y + 1] in keys.values():
                    y += 1
            if i == 'L':
                if [x - 1, y] in keys.values():
                    x -= 1
            if i == 'R':
                if [x + 1, y] in keys.values():
                    x += 1
        pos = [x, y]
        code.append(list(keys.keys())[list(keys.values()).index(pos)])

    return ''.join([str(x) for x in code])

keys = { 1: [0,0], 2: [1,0], 3: [2,0], 4: [0,1], 5: [1,1], 6: [2,1], 7: [0,2], 8: [1,2], 9: [2,2] }
keys_2 = { '1': [2, 0], '2': [1, 1], '3': [2, 1], '4': [3, 1], '5': [0, 2], '6': [1, 2], '7': [2, 2], '8': [3, 2], '9': [4, 2], 'A': [1, 3], 'B': [2, 3], 'C': [3, 3], 'D': [2, 4] }

pos_1 = [1, 1]
pos_2 = [0, 2]

print(f'Part 1: {get_code(keys, pos_1)}')
print(f'Part 2: {get_code(keys_2, pos_2)}')