lines = []

for line in open('data.txt'):
    lines.append(line.strip())

# Part 1
def part1():
    calibrations = []
    for line in lines:
        found = ''
        for char in line:
            if char.isnumeric():
                found += char
        found = found[0] + found[-1]
        calibrations.append(int(found))
    return sum(calibrations)

# Part 2
def part2():
    numbers = ['jippert', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    sum_calibrations = 0
    for line in lines:
        found = []
        for i, char in enumerate(line):
            if char.isnumeric():
                found.append((i, int(char)))

        for i, number in enumerate(numbers):
            index = 0
            while index < len(line):
                if number in line[index:]:
                    found.append((line[index:].find(number) + index, i))
                    index += line[index:].find(number) + 1
                else:
                    break

        found.sort()
        sum_calibrations += int(str(found[0][1]) + str(found[-1][1])) 

    return sum_calibrations 

print(part1())
print(part2())
