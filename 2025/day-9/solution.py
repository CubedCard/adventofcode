import numpy as np
import shapely
from itertools import combinations


def load_points(filename="data.txt"):
    return np.genfromtxt(filename, dtype=np.int64, comments=None, delimiter=",")


def largest_areas(points):
    polygon = shapely.Polygon(points)
    largest_area_p1 = 0
    largest_area_p2 = 0

    for p1, p2 in combinations(points, 2):
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

        area = (x_max - x_min + 1) * (y_max - y_min + 1)
        largest_area_p1 = max(largest_area_p1, area)

        if polygon.contains(shapely.box(x_min, y_min, x_max, y_max)):
            largest_area_p2 = max(largest_area_p2, area)

    return largest_area_p1, largest_area_p2


points = load_points()
part1, part2 = largest_areas(points)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
