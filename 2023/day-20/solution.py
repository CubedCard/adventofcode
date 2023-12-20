broadcaster = []
schema = []

for line in open('data.txt'):
    if line.startswith('broadcaster'):
        broadcaster = (line.split('->')[1].strip().split(', '))
    else:
        node, nodes = line.strip().split('->')
        nodes = [x.strip() for x in nodes.split(', ')]
        schema.append((node, nodes, False, {})) # (node, nodes, on / off, memory)

for node in schema:
    if node[0].startswith('&'):
        for node_ in schema:
            if node[0][1:].strip() in node_[1]:
                node[3][node_[0]] = 'low'

schema_part2 = schema.copy()

def get_node(node):
    for i, si in enumerate(schema):
        if si[0][1:].strip() == node.strip():
            return schema[i]
    return None

def find_by_name(name):
    for i, node in enumerate(schema):
        if node[0] == name:
            return i
    return -1

def do_cycle(broadcaster):
    high_pulses, low_pulses = 0, 1
    queue = []
    for i in broadcaster:
        queue.append((get_node(i), 0, None))
        low_pulses += 1

    while queue:
        node, pulse, prev = queue.pop(0)

        if node == None:
            continue

        if node[0].startswith('%'):
            if not pulse:
                new_pulse = 0 if node[2] else 1

                for i in node[1]:
                    queue.append((get_node(i), new_pulse, node))
                    high_pulses += 1 if new_pulse == 1 else 0
                    low_pulses += 1 if new_pulse == 0 else 0

                schema[find_by_name(node[0])] = (node[0], node[1], not node[2], node[3])

        elif node[0].startswith('&'):
            node[3][prev[0]] = 'low' if pulse == 0 else 'high'
            new_pulse = 1 if 'low' in node[3].values() else 0

            for i in node[1]:
                queue.append((get_node(i), new_pulse, node))
                high_pulses += 1 if new_pulse == 1 else 0
                low_pulses += 1 if new_pulse == 0 else 0

    return high_pulses, low_pulses

def part1():
    total_high_pulses, total_low_pulses = 0, 0
    for _ in range(1000):
        high_pulses, low_pulses = do_cycle(broadcaster)
        total_high_pulses += high_pulses
        total_low_pulses += low_pulses
    return total_high_pulses * total_low_pulses

def part2():
    cycles = 0
    while True:
        queue = []
        for i in broadcaster:
            queue.append((get_node(i), 0, None))

        while queue:
            node, pulse, prev = queue.pop(0)

            if node == None:
                if pulse == 0:
                    return cycles 
                continue

            if node[0].startswith('%'):
                if not pulse:
                    new_pulse = 0 if node[2] else 1

                    for i in node[1]:
                        queue.append((get_node(i), new_pulse, node))

                    schema[find_by_name(node[0])] = (node[0], node[1], not node[2], node[3])

            elif node[0].startswith('&'):
                node[3][prev[0]] = 'low' if pulse == 0 else 'high'
                new_pulse = 1 if 'low' in node[3].values() else 0

                for i in node[1]:
                    queue.append((get_node(i), new_pulse, node))
        cycles += 1


print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
