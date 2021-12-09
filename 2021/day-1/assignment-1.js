const fs = require('fs')

const makeArrayFromTextFile = (path) => {
  const text = fs.readFileSync(path, 'utf-8')
  const textByLine = text.split('\n')
  return textByLine
}

const array = makeArrayFromTextFile('./text.txt') 

let numberOfIncreases = 0;
for (let i = 1; i < array.length; i++) {
    if (parseInt(array[i]) > parseInt(array[i - 1])) {
        numberOfIncreases++;
    }
}

console.log(numberOfIncreases)
