import heapq
from collections import defaultdict

def add_computer_connection(network, computer1, computer2):
    network.setdefault(computer1, set()).add(computer2)
    network.setdefault(computer2, set()).add(computer1)

def find_interconnected_computers(network, computer1, computer2, triplets):
    triplets.update(frozenset([computer1, computer2, neighbor]) for neighbor in network[computer1] if neighbor in network[computer2])

def count_triplets_with_prefix(connections, prefix):
    network, triplets = defaultdict(set), set()
    
    for connection in connections:
        computer1, computer2 = connection.split("-")
        add_computer_connection(network, computer1, computer2)
        find_interconnected_computers(network, computer1, computer2, triplets)
    
    return sum(1 for triplet in triplets if any(c.startswith(prefix) for c in triplet))

def are_all_computers_connected(network, computers):
    return all([neighbor in network[computer] for computer in computers for neighbor in computers if computer < neighbor])

def find_largest_connected_group(connections):
    network = defaultdict(set)
    
    for connection in connections:
        computer1, computer2 = connection.split("-")
        add_computer_connection(network, computer1, computer2)

    computer_groups = [network[computer].union({computer}) for computer in network]
    priority_queue = [(-len(group), group) for group in computer_groups]
    
    while priority_queue:
        _, group = heapq.heappop(priority_queue)
        if are_all_computers_connected(network, group):
            return ",".join(sorted(group))
        priority_queue.extend(((-len(group) + 1, group - {computer}) for computer in group))

    return ""

def part_1(connections):
    return count_triplets_with_prefix(connections, "t")

def part_2(connections):
    return find_largest_connected_group(connections)

if __name__ == "__main__":
    connections = open('data.txt').read().splitlines()

    print(f"Part 1: {part_1(connections)}")
    print(f"Part 2: {part_2(connections)}")
