const read = require('../read');

const array = read.makeArrayFromTextFile('./text.txt');

let most_common = [...array];
let least_common = [...array];

while (most_common.length > 2) {
    for (let j = 0; j < array[0].length; j++) {
        let numberOfZeros = 0;
        let numberOfOnes = 0;
        for (let i = 0; i < most_common.length; i++) {
            if (most_common[i].charAt(j) == '0') {
                numberOfZeros++;
            } else {
                numberOfOnes++;
            }
        }
        if (numberOfOnes >= numberOfZeros) {
            deleteAllThatWithAt('0', j, most_common);
        } else {
            deleteAllThatWithAt('1', j, most_common);
        }
    }
}

while (least_common.length > 2) {
    for (let j = 0; j < array[0].length; j++) {
        let numberOfZeros = 0;
        let numberOfOnes = 0;
        for (let i = 0; i < least_common.length; i++) {
            if (least_common[i].charAt(j) == '0') {
                numberOfZeros++;
            } else {
                numberOfOnes++;
            }
        }
        if (numberOfOnes >= numberOfZeros) {
            deleteAllThatWithAt('1', j, least_common);
        } else {
            deleteAllThatWithAt('0', j, least_common);
        }
        console.log(least_common)
    }
}

function deleteAllThatWithAt(digit, pos, list) {
    for (let i = 0; i < list.length; i++) {
        if (list[i][pos] === digit) {
            list.splice(i, 1);
            i = i - 1;
        }
    }
}

console.log("most_common: " + most_common);
console.log("least_common: " + least_common);

let int1 = parseInt(most_common[0], 2);
let int2 = parseInt(111001000001, 2);
let multiply = int1 * int2;

console.log(multiply);
