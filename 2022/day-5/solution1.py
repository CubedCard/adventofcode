stack1 = ['Z', 'J', 'G']
stack2 = ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C']
stack3 = ['F', 'P', 'M', 'C', 'L', 'G', 'R']
stack4 = ['L', 'F', 'B', 'W', 'P', 'H', 'M']
stack5 = ['G', 'C', 'F', 'S', 'V', 'Q']
stack6 = ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L']
stack7 = ['H', 'F', 'S', 'B', 'V']
stack8 = ['F', 'J', 'Z', 'S']
stack9 = ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']

stacks = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

instructions = []

for line in open('./data.txt'):
    instructions.append(line.strip())


for instruction in instructions:
    array = instruction.split(' ')
    n = int(array[1])
    from_stack = int(array[3])
    pop = '' 
    to_stack = int(array[5])
    for i in range(0, n):
        pop = stacks[from_stack - 1].pop(len(stacks[from_stack - 1]) - 1)
        stacks[to_stack - 1].append(pop)

output = ''

for stack in stacks:
    output += stack.pop(len(stack) - 1)

print(output)
