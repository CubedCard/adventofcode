# to low: 71820

import re
import numpy as np

data = open('data.txt', 'r').read()

time_pattern = re.compile(r'Time:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)')
distance_pattern = re.compile(r'Distance:\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)')

time_match = time_pattern.search(data)
distance_match = distance_pattern.search(data)

def getTimesAndDistances():
    if time_match and distance_match:
        times = list(map(int, time_match.groups()))
        distances = list(map(int, distance_match.groups()))
        return times, distances
    else:
        return [], []


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
    times, distances = getTimesAndDistances()
    total_time = ''
    total_distance = ''
    for time in times:
        total_time += str(time)
    for distance in distances:
        total_distance += str(distance)

    total_time = int(total_time)
    total_distance = int(total_distance)

    return part1([total_time], [total_distance])


times, distances = getTimesAndDistances()
print(part1(times, distances))
print(part2())
