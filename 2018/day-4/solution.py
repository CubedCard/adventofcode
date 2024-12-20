import re
from collections import defaultdict

logs = open('data.txt').read().splitlines()
logs.sort()

guard_id, sleep_start, guard_minutes = None, None, []

for log in logs:
    match = re.match(r"\[(\d+-\d+-\d+ \d+:\d+)\] (.*)", log)
    timestamp, action = match.groups()

    if "Guard" in action:
        guard_id = int(re.search(r"#(\d+)", action).group(1))
    elif action == "falls asleep":
        sleep_start = int(timestamp.split(":")[1])
    elif action == "wakes up":
        wake_time = int(timestamp.split(":")[1])
        for minute in range(sleep_start, wake_time):
            guard_minutes.append((guard_id, minute))

def get_count(g):
    counts = {i: 0 for i in range(60)}
    for guard, minute in guard_minutes:
        if guard == g:
            counts[minute] += 1
    return max(counts, key=counts.get)

def part_1():
    guards = set([x[0] for x in guard_minutes])
    minutes_per_guard = [(guard, sum([1 for x in guard_minutes if x[0] == guard])) for guard in guards]
    max_guard = max(minutes_per_guard, key=lambda x: x[1])
    
    return get_count(max_guard[0]) * max_guard[0]

def part_2():
    guards = set([x[0] for x in guard_minutes])
    guard_max = {guard: 0 for guard in guards}

    for guard in guards:
        guard_max[guard] = get_count(guard)

    most_asleep = max(guard_max, key=lambda guard: sum(1 for g, minute in guard_minutes if g == guard and minute == guard_max[guard]))

    return most_asleep * guard_max[most_asleep]

print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")