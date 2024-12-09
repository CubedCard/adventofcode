data = open('data.txt').read().strip()

def get_output():
    output = []
    for i, char in enumerate(data, 1):
        val = i // 2 + 1 if i % 2 else 0
        output.append((val, int(char)))
    return output

def move_left(output):
    number_count = sum(1 for char in output if char)

    k, l = 0, len(output) - 1
    while k < number_count and l >= number_count:
        if output[k] == 0:
            while output[l] == 0:
                l -= 1
            temp = output[k]
            output[k] = output[l]
            output[l] = temp
            l -= 1
        k += 1

    return output

def redistribute(output):
    for i in range(len(output) - 1, -1, -1):
        for j in range(i):
            i_val, i_size = output[i]
            j_val, j_size = output[j]

            if i_val and not j_val and i_size <= j_size:
                output[i] = (0, i_size)
                output[j] = (0, j_size - i_size)
                output.insert(j, (i_val, i_size))
    return output 

def convert_to_list(data):
    flat_list = []
    for val, size in data:
        flat_list.extend([val] * size)
    return flat_list

def total(output):
    return sum(i * (val - 1) for i, val in enumerate(output) if val)

def part_1():
    output_list = convert_to_list(get_output())
    moved = move_left(output_list)
    return total(moved)

def part_2():
    output = get_output()
    redistributed = redistribute(output)
    output_list = convert_to_list((num, size) for num, size in redistributed if size > 0)
    return total(output_list) 

print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')