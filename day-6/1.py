class Fish:
    def __init__(self, age):
        self.age = age
    def dayPasses(days):
        self.age = self.age - days
        return self.age

ages = [
  1, 1, 1, 1, 3, 1, 4, 1, 4, 1, 1, 2, 5, 2, 5, 1, 1, 1, 4, 3, 1, 4, 1, 1, 1, 1,
  1, 1, 1, 2, 1, 2, 4, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 5, 1, 1, 2, 1, 5, 1, 1, 1,
  1, 1, 1, 1, 1, 4, 3, 1, 1, 1, 2, 1, 1, 5, 2, 1, 1, 1, 1, 4, 5, 1, 1, 2, 4, 1,
  1, 1, 5, 1, 1, 1, 1, 5, 1, 3, 1, 1, 4, 2, 1, 5, 1, 2, 1, 1, 1, 1, 1, 3, 3, 1,
  5, 1, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 4, 1, 4, 3, 1, 1, 1, 4, 1, 2, 1, 1, 1,
  2, 1, 1, 1, 1, 5, 1, 1, 3, 5, 1, 1, 5, 2, 1, 1, 1, 1, 1, 4, 4, 1, 1, 2, 1, 1,
  1, 4, 1, 1, 1, 1, 5, 3, 1, 1, 1, 5, 1, 1, 1, 4, 1, 4, 1, 1, 1, 5, 1, 1, 3, 2,
  2, 1, 1, 1, 4, 1, 3, 1, 1, 1, 2, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 2, 1, 4, 1,
  1, 1, 1, 1, 4, 1, 1, 2, 4, 2, 1, 2, 3, 1, 3, 1, 1, 2, 1, 1, 1, 3, 1, 1, 3, 1,
  1, 4, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 1, 3, 1, 1, 5, 1, 1, 3, 1, 1, 1, 1, 5, 1,
  1, 1, 1, 1, 2, 3, 4, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 3, 2, 2, 1, 3, 5,
  1, 1, 4, 4, 1, 3, 4, 1, 2, 4, 1, 1, 3, 1,
]

# start program

# fish array:
fishes = []

# put all fishes in the array with the given age
for age in ages:
    fishes.append(Fish(age))

def dayPasses(fish, days):
    fish.age = fish.age - days
    return fish.age

for x in range(0,256):
    print(x)
    born = 0
    for fish in fishes:
        if dayPasses(fish, 1) < 0:
            fish.age = 6
            born += 1
    for x in range(0, born):
        fishes.append(Fish(8))

# print result
print(len(fishes))
