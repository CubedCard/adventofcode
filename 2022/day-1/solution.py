array = []

for file in open('./data.txt'):
    line = file.strip()
    array.append(line)

most_calories = 0
calories = 0 

for item in array:
    if item == '':
        most_calories = max(most_calories, calories)
        calories = 0
    else:
        calories += int(item)

print(most_calories)
