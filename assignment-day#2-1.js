const fs = require('fs')

const makeArrayFromTextFile = (path) => {
  const text = fs.readFileSync(path, 'utf-8')
  const textByLine = text.split('\n')
  return textByLine
}

const array = makeArrayFromTextFile('./text2.txt') 

let pos_hor = 0;
let depth = 0;

for (let i = 0; i < array.length; i++) {
    let line = array[i].split(' ');
    let command = line[0];
    let number = parseInt(line[1]);

    console.log(command)
    console.log(number)
    console.log(pos_hor)
    console.log(depth)

    if (command === "forward") pos_hor += number;
    else if (command === "up") depth -= number;
    else if (command === "down") depth += number;
}

console.log(pos_hor);
console.log(depth);
console.log(pos_hor * depth);


