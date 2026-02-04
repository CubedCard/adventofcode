from collections import defaultdict


def load_graph(filename="data.txt"):
    graph = defaultdict(list)
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            node = parts[0][:-1]
            graph[node] = parts[1:]
    return graph


def count_paths(node, graph, target, cache=None):
    if cache is None:
        cache = {}
    if node == target:
        return 1
    if node in cache:
        return cache[node]
    total = sum(count_paths(nei, graph, target, cache) for nei in graph[node])
    cache[node] = total
    return total


def part1(graph):
    return count_paths("you", graph, "out")


def part2(graph):
    to_fft = count_paths("svr", graph, "fft")
    to_dac = count_paths("fft", graph, "dac")
    to_out = count_paths("dac", graph, "out")
    return to_fft * to_dac * to_out


graph = load_graph()
print(f"Part 1: {part1(graph)}")
print(f"Part 2: {part2(graph)}")
