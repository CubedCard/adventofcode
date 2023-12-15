strings = open('data.txt').read().strip().split(',')

def hash_string(string):
    prev = 0
    for char in string:
        val = (ord(char) + prev) * 17
        while val > 255:
            val -= 256
        prev = val
    return prev

def part1():
    total = 0
    for string in strings:
        total += hash_string(string)
    return total


def get_total_focussing_power(boxes):
    total = 0
    for box in boxes:
        for j, item in enumerate(boxes[box]):
            box_label, focas_length = hash_string(item.split('=')[0]), int(item.split('=')[1])
            val = focas_length * (j + 1) * (box_label + 1)
            total += val
    return total

def part2():
    boxes = {}
    for string in strings:
        if '-' in string:
            label = string.split('-')[0]
            box_label = hash_string(label)
            new_stack = []
            if box_label in boxes:
                for item in boxes[box_label]:
                    if not item.startswith(label):
                        new_stack.append(item)
                boxes[box_label] = new_stack
        elif '=' in string:
            label = string.split('=')[0]
            box_label = hash_string(label)
            if box_label not in boxes:
                boxes[box_label] = []
            for i, item in enumerate(boxes[box_label]):
                if item.startswith(label):
                    boxes[box_label][i] = string
                    break
            else: 
                boxes[box_label].append(string)
    return get_total_focussing_power(boxes)

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
