import re

lines = []

for line in open('data.txt'):
    lines.append(line.strip())

# Extract seeds
seeds_match = re.search(r"seeds: (.+)", lines[0])
seed_values = list(map(int, seeds_match.group(1).split())) if seeds_match else []

# Extract tuples
tuple_matches = re.findall(r"(\w+)-to-(\w+) map:\n(.+?)\n\n", '\n'.join(lines), re.DOTALL)

tuple_lists = []
for tpl in tuple_matches:
    name = tpl[1]
    matrix = [list(map(int, line.split())) for line in tpl[2].split('\n') if line]
    tuple_lists.append((name, *matrix))

def part1(seeds):
    location_values = []
    for seed in seeds:
        journey = [seed]
        current_val = seed
        for tpl in tuple_lists:
            for i in range(1, len(tpl)):
                max_val = int(tpl[i][1]) + int(tpl[i][2] - 1)
                if tpl[i][1] <= current_val <= max_val:
                    current_val = int(tpl[i][0]) + int(current_val) - int(tpl[i][1])
                    break
            journey.append(current_val)
        location_values.append(current_val)

    return min(location_values)

def part2():
    seeds = []
    # loop through every other seed
    for i in range(0, len(seed_values), 2):
        for j in range(seed_values[i], seed_values[i] + seed_values[i+1] - 1):
            seeds.append(j)
    return part1(seeds)


print(part1(seed_values))
print(part2())
