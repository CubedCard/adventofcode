from directory import Directory

terminal_output = []
directories = set()

for file in open('./data.txt'):
    terminal_output.append(file.strip())

pwd = Directory(None, '/') 
directories.add(pwd)

for line in terminal_output:
    if line.startswith('$'):
        if line.startswith('$ cd'):
            if '..' in line:
                if pwd.parent:
                    pwd = pwd.parent
            elif '/' in line:
                for directory in directories:
                    if directory.name == '/':
                        pwd = directory
            else:
                found = False
                for directory in directories:
                    if directory.name == line.split()[-1]:
                        found = True
                        pwd = directory
                if not found:
                    new_dir = Directory(pwd, line.split()[-1])
                    pwd.directories.add(new_dir)
                    directories.add(new_dir)
                    pwd = new_dir
    else:
        if line.startswith('dir'):
            found = False
            for directory in directories:
                if directory.name == line.split()[-1]:
                    found = True
                    pwd.directories.add(directory)
            if not found:
                new_dir = Directory(pwd, line.split()[-1])
                pwd.directories.add(new_dir)
                directories.add(new_dir)
                pwd.directories.add(Directory(pwd, line.split()[-1]))
        else:
            pwd.files.add(int(line.split()[0]))

total = 0

for directory in directories:
    size = directory.getSize()
    if size <= 100000:
        total += size
        print(directory.name, size)

print(total)
