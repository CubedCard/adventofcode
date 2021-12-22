const numberOfRollsPerPlayer = 3
const boardSize = 10
let bigDie = 0
let totalRolls = 0

let player1 = 5
let player2 = 6

while (condition()) {
    player1 += (roll() + player1 % boardSize) % boardSize;
    if (!condition()) break;
    player2 += (roll() + player2 % boardSize) % boardSize;
}

console.log(player1, player2, totalRolls);

function condition() {
    return player1 < 1000 && player2 < 1000;
}

function die() {
    if (bigDie > 100) {
        bigDie = 0;
    }
}

function roll() {
    total = 0
    for (let i = 0; i < numberOfRollsPerPlayer; i++) {
        die();
        bigDie++;
        total += bigDie;
        totalRolls++;
    }
    return total;
}

