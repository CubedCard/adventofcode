bigDie = 1
numberOfRollsPerPlayer = 3
boardSize = 10
totalRolls = 0

print("Welcome to day 21 of Advent of Code")

player1 = 5
player2 = 6

def roll():
    total = 0
    for x in range(numberOfRollsPerPlayer):
        if bigDie > 100:
            bigDie = 1
        total += bigDie
        bigDie += 1
        totalRolls += 1
    return total % boardSize

while (player1 < 1000 and player2 < 1000):
    player1 += roll() 
    player2 += roll() 

print(player1, player2, totalRolls)
