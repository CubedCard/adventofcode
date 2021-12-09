const fs = require('fs')

const makeArrayFromTextFile = (path) => {
  const text = fs.readFileSync(path, 'utf-8')
  const textByLine = text.split('\n')
  return textByLine
}

const array = makeArrayFromTextFile('./text.txt') 

let numberOfIncreases = 0;
for (let i = 0; i < array.length - 3; i++) {
    let firstPart = parseInt(array[i]) + parseInt(array[i + 1]) + parseInt(array[i + 2])
    let secondPart = parseInt(array[i + 1]) + parseInt(array[i + 2]) + parseInt(array[i + 3])
    if (secondPart > firstPart) {
        numberOfIncreases++;
    }
}

console.log(numberOfIncreases)
