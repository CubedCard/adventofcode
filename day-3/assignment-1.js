const read = require('../read');

const array = read.makeArrayFromTextFile('./text.txt');

let gamma_rate = "";
let epsilon_rate = "";

for (let j = 0; j < array[0].length; j++) {
    let numberOfZeros = 0;
    let numberOfOnes = 0;
    for (let i = 0; i < array.length; i++) {
        if (array[i].charAt(j) == '0') {
            numberOfZeros++;
        } else {
            numberOfOnes++;
        }
    }
    if (numberOfOnes > numberOfZeros) {
        gamma_rate += "1";
        epsilon_rate += "0";
    } else {
        gamma_rate += "0";
        epsilon_rate += "1";
    }
}

console.log(gamma_rate);
console.log(epsilon_rate);

let int1 = parseInt(gamma_rate, 2);
let int2 = parseInt(epsilon_rate, 2);
let binary = (int1 * int2).toString(2);
var digit = parseInt(binary, 2);

console.log(digit);
