instructions = []

for line in open('./data2.txt'):
    instructions.append(line.strip())

next_cycle = 0

X = 1
total = 0

plus_string = ''

for i in range(len(instructions)):
    X += next_cycle
    next_cycle = 0
    if (i + 1) == 10:
        total += X * (i + 1)
        print(i + 1, '*', X, '=', total)
    elif (i + 1 - 20) % 40 == 0 and i + 1 - 20 > 0:
        total += X * (i + 1)
        print(i + 1, '*', X, '=', total)
    if instructions[i].startswith('addx'):
        next_cycle = int(instructions[i].split(' ')[1])
print(total)

