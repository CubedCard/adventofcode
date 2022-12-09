class Directory {
  constructor(parent, name) {
    this.parent = parent;
    this.name = name;
    this.files = new Set();
    this.directories = new Set();
  }

  getSize() {
    let size = 0;
    for (let file of this.files) {
      size += file;
    }
    for (let directory of this.directories) {
      size += directory.getSize();
    }
    return size;
  }
}

let terminalOutput = [];
let directories = new Set();

const fs = require('fs');

terminalOutput = fs.readFileSync('./data.txt').split('\n');

let pwd = new Directory(null, "/");

for (let line of terminalOutput) {
  if (line.startsWith("$")) {
    if (line.startsWith("$ cd")) {
      if (".." in line) {
        if (pwd.parent) {
          pwd = pwd.parent;
        }
      } else if ("/" in line) {
        for (let directory of directories) {
          if (directory.name == "/") {
            pwd = directory;
          }
        }
      } else {
        let found = false;
        for (let directory of directories) {
          if (directory.name == line.split()[-1]) {
            found = true;
            pwd = directory;
          }
        }
        if (found == false) {
          let new_dir = new Directory(pwd, line.split()[-1]);
          pwd.directories.add(new_dir);
          directories.add(new_dir);
          pwd = new_dir;
        }
      }
    } else {
      if (line.startsWith("dir")) {
        let found = false;
        for (let directory of directories) {
          if (directory.name == line.split()[-1]) {
            found = true;
            pwd.directories.add(directory);
          }
        }
        if (!found) {
          let new_dir = new Directory(pwd, line.split()[-1]);
          pwd.directories.add(new_dir);
          directories.add(new_dir);
          pwd.directories.add(new Directory(pwd, line.split()[-1]));
        }
      } else {
        pwd.files.add(parseInt(line.split()[0]));
      }
    }
  }
}

let total = 0;

for (let directory of directories) {
  let size = directory.getSize();
  if (size <= 100000) {
    total += size;
    console.log(directory.name, size);
  }
}

console.log(total);
