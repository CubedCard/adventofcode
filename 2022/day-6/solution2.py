data = ''

for file in open('./data.txt'):
    data += file

buffer = []
processed = 0

for char in data:
    if len(set(buffer)) == 14:
        break
    if len(buffer) == 14:
        buffer.pop(0)
    buffer.append(char)
    processed += 1

print(buffer)
print(processed)
