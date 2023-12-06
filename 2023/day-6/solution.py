import re
import numpy as np

data = open('data.txt', 'r').read().split('\n')

times_text, distances_text = data[0], data[1]
times = [int(x) for x in re.findall(r'\d+', times_text)]
distances = [int(x) for x in re.findall(r'\d+', distances_text)]

def part1(times, distances):
    scores = []
    for time in times:
        speeds = []
        for i in range(int(time) + 1):
            distance_travelled = i * (time - i)
            if distance_travelled > distances[times.index(time)]:
                speeds.append(i)
        scores.append(len(speeds))
    result = np.prod(scores)
    return result

def part2():
    total_time = ''
    total_distance = ''
    for time in times:
        total_time += str(time)
    for distance in distances:
        total_distance += str(distance)

    total_time = int(total_time)
    total_distance = int(total_distance)

    return part1([total_time], [total_distance])


print(part1(times, distances))
print(part2())
