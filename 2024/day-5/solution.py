import re
import itertools
from collections import defaultdict, deque

def is_before(a, b, text):
    if a not in text:
        return False
    return text.index(a) < text.index(b)

def parse_input(file):
    a, b = open(file).read().split("\n\n")
    a, b = a.split('\n'), b.split('\n')

    rules = [rule.split("|") for rule in a]
    pages = [page.split(",") for page in b]

    return rules, pages

def get_rule(a, rules):
    return [rule for rule in rules if rule[0] == a]

def get_middle(page):
    return page[len(page) // 2]

def valid(page, rules):
    for num in page:
        rule = get_rule(num, rules)
        for r in rule:
            if is_before(r[1], num, page):
                return False
    return True

def part_1(file):
    rules, pages = parse_input(file)

    middles = []
    for page in pages:
        if valid(page, rules):
            middles.append(get_middle(page))

    return sum([int(m) for m in middles if m != ''])

def topological_sort(numbers, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for num in numbers:
        in_degree[num] = 0

    for rule in rules:
        a, b = rule[0], rule[1]
        if a in numbers and b in numbers:
            graph[a].append(b)
            in_degree[b] += 1
    
    queue = deque([node for node in numbers if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def part_2(file): 
    rules, pages = parse_input(file)

    middles = []
    for page in pages:
        if not valid(page, rules):
            middles.append(get_middle(topological_sort(page, rules)))
    
    return sum([int(m) for m in middles if m != ''])

print(f"Part 1: {part_1('data.txt')}")
print(f"Part 2: {part_2('data.txt')}")

assert part_1('data.txt') == 5948
assert part_2('data.txt') == 3062