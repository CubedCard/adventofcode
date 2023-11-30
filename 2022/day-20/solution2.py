class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

cords = []

for line in open('data.txt'):
    node = Node(int(line.strip()) * 811589153)
    cords.append(node)
    node.prev = cords[-2] if len(cords) > 1 else None
    if node.prev:
        node.prev.next = node

cords[0].prev = cords[-1]
cords[-1].next = cords[0]

def print_cords(arr):
    printed = []
    output = []
    cord = arr[0]
    while cord not in printed:
        output.append(cord.data)
        printed.append(cord)
        cord = cord.next
    print(output)


def move_before_zero_to_end(arr):
    index_of_zero = -1
    for i in range(len(arr)):
        if arr[i] == '0':
            index_of_zero = i
            break

    if index_of_zero != -1:
        arr_before_zero = arr[:index_of_zero]
        arr_after_zero = arr[index_of_zero:]
        arr = arr_after_zero + arr_before_zero
        return arr

    return arr

def sum(arr):
    sum = 0
    for i in arr:
        sum += int(i)
    return sum

def get_1000_2000_3000(cords):
    node = cords[0]
    while int(node.data) != 0:
        node = node.next
    output = []
    for i in range(1, 3001):
        node  = node.next
        if i == 1000 or i == 2000 or i == 3000:
            output.append(node.data)
    return output

for _ in range(10):
    for cord in cords:
        steps = cord.data
        if steps > 0:
            for _ in range(steps):
                cord.prev.next = cord.next
                cord.next.prev = cord.prev
                cord.prev = cord.next
                cord.next = cord.next.next
                cord.next.prev = cord
                cord.prev.next = cord
        else:
            for _ in range(abs(steps)):
                cord.prev.next = cord.next
                cord.next.prev = cord.prev
                cord.next = cord.prev
                cord.prev = cord.prev.prev
                cord.next.prev = cord
                cord.prev.next = cord

print(sum(get_1000_2000_3000(cords)))
