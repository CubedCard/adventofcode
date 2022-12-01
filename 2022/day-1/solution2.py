array = []

for file in open('./data.txt'):
    line = file.strip()
    array.append(line)

calories_per_elf = []
calories = 0 

for item in array:
    if item == '':
        calories_per_elf.append(calories)
        calories = 0
    else:
        calories += int(item)

calories_per_elf.sort(reverse=True)

top_three_calories = calories_per_elf[0] + calories_per_elf[1] + calories_per_elf[2]

print(top_three_calories)
