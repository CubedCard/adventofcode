import math 
import re

workflows = []
parts = []
parts_maps = []

ids = ['x', 'm', 'a', 's']

data = open('data.txt', 'r').read().split('\n\n')

for line in data[0].split('\n'):
    workflows.append(line.strip())

for line in data[1].split('\n'):
    parts.append(line.strip())

for part in parts:
    pattern = r"\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}"

    match = re.match(pattern, part)

    if match:
        x_value = int(match.group(1))
        m_value = int(match.group(2))
        a_value = int(match.group(3))
        s_value = int(match.group(4))

        my_map = {"x": x_value, "m": m_value, "a": a_value, "s": s_value}
        parts_maps.append(my_map)

def get_workflow(workflow_id):
    for workflow in workflows:
        if workflow[:workflow.find('{')] == workflow_id:
            return workflow

def get_workflow_condition(workflow, condition_id):
    for i, char in enumerate(workflow):
        if char == condition_id:
            return i
    return -1

def use_regex(input_text):
    pattern = re.compile(r"^[a-zA-Z]+{(?:[xmas][<>]\d+:[^,]+(?:,[xmas][<>]\d+:[^,]+){0,3}),[a-zA-Z]+}$", re.IGNORECASE)
    return pattern.match(input_text)


def get_next_workflow(input_string, parts):
    pattern = r"([a-zA-Z]+){((?:[xmas][<>]\d+:[^,]+(?:,[xmas][<>]\d+:[^,]+){0,3}),([a-zA-Z]+))}"
    match = re.search(pattern, input_string)

    if match:
        content = match.group(2)
        conditions = re.findall(r'([xmas])([<>])(\d+):([^,]+)', content)
        parsed_data = [(condition, operator, value, result) for condition, operator, value, result in conditions]
        default = match.group(3)
        for condition, operator, value, result in parsed_data:
            parts_value = parts[condition]
            if operator == '<':
                if parts_value < int(value):
                    return result
            elif operator == '>':
                if parts_value > int(value):
                    return result
        return default
    else:
        print(f'No match found in "{input_string}".')

def part1():
    accepted = 0
    for parts_map in parts_maps:
        current_workflow = get_workflow('in')
        result = None 
        while result != 'A' and result != 'R':
            result = get_next_workflow(current_workflow, parts_map)
            if result == 'A':
                for id in ids:
                    accepted += parts_map[id]
            elif result == 'R':
                break
            else:
                current_workflow = get_workflow(result)
    return accepted

def get_parsed_data(workflow):
    pattern = r"([a-zA-Z]+){((?:[xmas][<>]\d+:[^,]+(?:,[xmas][<>]\d+:[^,]+){0,3}),([a-zA-Z]+))}"
    match = re.search(pattern, workflow)

    if match:
        content = match.group(2)
        conditions = re.findall(r'([xmas])([<>])(\d+):([^,]+)', content)
        parsed_data = [(condition, operator, int(value), result) for condition, operator, value, result in conditions]
        default = match.group(3)
        return parsed_data, default

def replace_range(ranges, condition, item):
    replaced_ranges = list(ranges)
    replaced_ranges[condition] = item
    return replaced_ranges

def part2():
    queue = [('in', [range(1, 4001)] * 4)]
    accepted = 0
    while queue:
        workflow_id, ranges = queue.pop(0)
        if workflow_id == 'A':
            accepted += math.prod(list(map(len, ranges)))
            continue
        elif workflow_id == 'R':
            continue
        conditions, default = get_parsed_data(get_workflow(workflow_id))
        for condition, operator, value, result in conditions:
            condition_index = ids.index(condition)
            current_range = ranges[condition_index]
            if value not in current_range:
                continue
            is_greater_than = operator == '>'
            new_range = [current_range.start, value + is_greater_than, current_range.stop]
            new_ranges = range(*new_range[:-1]), range(*new_range[1:])
            if is_greater_than:
                new_ranges = new_ranges[::-1]
            queue.append((result, replace_range(ranges, condition_index, new_ranges[0])))
            ranges[condition_index] = new_ranges[1]
        queue.append((default, ranges))
    return accepted


print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')
