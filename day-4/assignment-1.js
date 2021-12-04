const read = require('../read')
const fs = require('fs')

const bingoCardSize = 5;

const makeArrayFromTextFile = (path) => {
  const text = fs.readFileSync(path, 'utf-8')
  const textByLine = text.split(/[\n\r]+/g)
  return textByLine
}

let numbers = [15,61,32,33,87,17,56,73,27,83,0,18,43,8,86,37,40,6,93,25,14,68,64,57,39,46,55,13,21,72,51,81,78,79,52,65,36,92,97,28,9,24,22,69,70,42,3,4,63,50,91,16,41,94,77,85,49,12,76,67,11,62,99,54,95,1,74,34,88,89,82,48,84,98,58,44,5,53,7,19,29,30,35,26,31,10,60,59,80,71,45,38,20,66,47,2,23,96,90,75];
let array = makeArrayFromTextFile("./text.txt");
let chosenNumbers = [];

// loop: every turn, add the next number of numbers to chosenNumbers 
// check if the first 25 contain more than 5 of the chosenNumbers.
// true: check if bingo
// false: next
let numberOfPlayers = (array.length - 1) / bingoCardSize;

let players = []

// creating a better array out of the array
for (let i = 0; i < numberOfPlayers; i++) {
    for (let j = i; j < i + bingoCardSize; j++) {
        let player = [];
        let text = array[j];
        let textByLine = text.split(' ');
        for (let h = 0; h < textByLine.length; h++) {
            if (textByLine[h] == '') textByLine.splice(h, 1);
        }
        players.push(textByLine);
    }
}

for (let i = 0; i < numbers.length; i++) {
    chosenNumbers.push(numbers[i]);
    for (let h = 0; h < chosenNumbers.length; h++) {
        checkIfSomeoneWon(chosenNumbers[h]);
    }
}

function checkIfSomeoneWon(number) {
    for (let i = 0; i < numberOfPlayers; i++) {
        let won = true;
        for (let h = 0; h < bingoCardSize; h++) {
            if (players[i][h] != number) won = false; 
        }
        if (won == true) {
            console.log("winner!: " + i);
        }
    }
}

