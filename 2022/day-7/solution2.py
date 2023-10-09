from collections import defaultdict

terminal_output = []

for file in open('./data.txt'):
    terminal_output.append(file.strip())

path = []
size = defaultdict(int)

max_size = 70000000
min_unused = 30000000

for line in terminal_output:
    if line.startswith('$'):
        if line.startswith('$ cd'):
            if '..' in line:
                path.pop()
            else: 
                path.append(line.split()[2])
    else:
        if line.startswith('dir'):
            continue
        else:
            file_size = int(line.split()[0])
            for i in range(1, len(path)+1):
                size['/'.join(path[:i])] += file_size

min_free = max_size - min_unused
used = size['/']
to_delete = abs(min_free - used)

ans = max_size 
for k,v in size.items():
    if v > to_delete:
        ans = min(ans, v)
print(ans)

