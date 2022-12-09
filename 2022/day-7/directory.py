class Directory():
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.files = set()
        self.directories = set()

    def getSize(self):
        size = sum(self.files)
        dirs = self.directories
        while len(dirs) > 0:
            for dir_ in dirs:
                size += sum(dir_.files)
                dirs = dir_.directories
        return size
