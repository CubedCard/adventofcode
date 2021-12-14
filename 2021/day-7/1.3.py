class Crab():
    def __init__(self, pos):
        self.pos = pos 

crabs = []

for crab in open('./text.txt'):
    numbers = crab.split(",")
    for number in numbers:
        crabs.append(int(number.strip()))

realcrabs = []

for number in crabs:
    realcrabs.append(Crab(number))

# calculate the total 
total = 0 
for crab in crabs:
    total += crab

average = total / len(crabs)

print(average)

fuel = 0

for crab in realcrabs:
    times = 1
    while crab.pos != average:
        if crab.pos > average:
            crab.pos = crab.pos - 1
        elif crab.pos < average:
            crab.pos = crab.pos + 1
        fuel += times 
        times += 1


# print all crabs:
#for crab in realcrabs:
#    print(crab.pos)

print(fuel)


