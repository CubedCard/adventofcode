lines = [line.strip() for line in open('data.txt')]

two = 0
three = 0

for line in lines:
    counts = [line.count(char) for char in line]
    if 2 in counts:
        two += 1
    if 3 in counts:
        three += 1

print(two * three)

for x in lines:
    for y in lines:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])
            print(''.join(ans))
            print(x, y)