from collections import defaultdict

terminal_output = []

for file in open('./data.txt'):
    terminal_output.append(file.strip())

path = []
size = defaultdict(int)

for line in terminal_output:
    if line.startswith('$'):
        if line.startswith('$ cd'):
            if '..' in line:
                path.pop()
            else: 
                path.append(line[4:])
    else:
        if line.startswith('dir'):
            continue
        else:
            file_size = int(line.split()[0])
            for i in range(1, len(path)+1):
                size['/'.join(path[:i])] += file_size

ans = 0
for k,v in size.items():
    if v <= 100000:
        ans += v
print(ans)

