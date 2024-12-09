data = open('text.txt').read().strip().split(', ')

angle = 0
position = [0, 0]
visited = []
directions = ((1, 1),(0, 1),(1, -1),(0, -1))

visited_twice = []

def appendposition(distance, index, increment):
	for _ in range(distance):
		position[index] += increment
		if tuple(position) in visited:
			visited_twice.append(sum(abs(p) for p in position))
		visited.append(tuple(position))

for d in data:
	direction = d[0]
	distance  = int(d[1:])
	
	angle += 1 if direction == "R" else -1
	angle %= 4

	appendposition(distance, *directions[angle])

print(f'Part 1: {visited_twice[0]}')
print(f'Part 2: {sum(abs(p) for p in position)}')
