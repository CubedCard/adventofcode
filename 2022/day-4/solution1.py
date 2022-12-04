array = []

for line in open('./data.txt'):
    array.append(line.strip())

overlaps = 0

for pair in array:
    first_range, second_range = pair.split(',')
    first1, second1 = first_range.split('-')
    first2, second2 = second_range.split('-')

    first_list = list(range(int(first1), int(second1) + 1))
    second_list = list(range(int(first2), int(second2) + 1))

    if set(first_list) <= set(second_list) or set(second_list) <= set(first_list):
        overlaps += 1

print(overlaps)
