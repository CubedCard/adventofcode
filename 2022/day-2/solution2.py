array = []

for file in open('./data.txt'):
    line = file.strip()
    array.append(line)

points = 0
rock = 1
paper = 2
scissors = 3

lost = 0
draw = 3
won = 6

for item in array:
    player1, player2 = item.split(' ')
    player1 = player1.strip()
    player2 = player2.strip()

    if player1 == 'A' and player2 == 'Z':
        points += won 
        points += paper 
    elif player1 == 'A' and player2 == 'Y':
        points += draw 
        points += rock
    elif player1 == 'A' and player2 == 'X':
        points += lost
        points += scissors
    elif player1 == 'B' and player2 == 'X':
        points += lost
        points += rock 
    elif player1 == 'B' and player2 == 'Z':
        points += won
        points += scissors
    elif player1 == 'B' and player2 == 'Y':
        points += draw
        points += paper
    elif player1 == 'C' and player2 == 'Y':
        points += draw 
        points += scissors
    elif player1 == 'C' and player2 == 'X':
        points += lost
        points += paper
    elif player1 == 'C' and player2 == 'Z':
        points += won
        points += rock

print(points)
