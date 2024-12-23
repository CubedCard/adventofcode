import heapq
from collections import defaultdict

def add_computer_connection(network, computer1, computer2):
    if computer1 not in network:
        network[computer1] = {computer2}
    else:
        network[computer1].add(computer2)
    
    if computer2 not in network:
        network[computer2] = {computer1}
    else:
        network[computer2].add(computer1)

def find_interconnected_computers(network, computer1, computer2, triplets):
    [triplets.add(frozenset([computer1, computer2, neighbor])) for neighbor in network[computer1] if neighbor in network[computer2]]

def count_triplets_with_prefix(connections, prefix):
    network = defaultdict(set)
    triplets = set()
    
    for connection in connections:
        computer1, computer2 = connection.split("-")
        add_computer_connection(network, computer1, computer2)
        find_interconnected_computers(network, computer1, computer2, triplets)
    
    count = 0
    for triplet in triplets:
        for computer in triplet:
            if computer.startswith(prefix):
                count += 1
                break
    return count

def are_all_computers_connected(network, computers):
    return all([neighbor in network[computer] for computer in computers for neighbor in computers if computer < neighbor])

def find_largest_connected_group(connections):
    network = defaultdict(set)
    
    for connection in connections:
        computer1, computer2 = connection.split("-")
        add_computer_connection(network, computer1, computer2)

    computer_groups = [network[computer].union({computer}) for computer in network]
    priority_queue = [(-len(neighbors), neighbors) for neighbors in computer_groups]
    
    while priority_queue:
        priority, group = heapq.heappop(priority_queue)
        if are_all_computers_connected(network, group):
            return ",".join(sorted(group))
        for computer in group:
            heapq.heappush(priority_queue, (priority + 1, group - {computer}))
    
    return ""

def part_1_solution(connections):
    return count_triplets_with_prefix(connections, "t")

def part_2_solution(connections):
    return find_largest_connected_group(connections)

if __name__ == "__main__":
    connections = open('data.txt').read().splitlines()

    print(f"Part 1: {part_1_solution(connections)}")
    print(f"Part 2: {part_2_solution(connections)}")