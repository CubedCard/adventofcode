import re

cards = []
pattern = re.compile(r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)")

for line in open('data.txt'):
    match = pattern.match(line)

    if match:
        card_number = int(match.group(1))
        winning_numbers = list(map(int, match.group(2).split()))
        your_numbers = list(map(int, match.group(3).split()))

        cards.append((card_number, winning_numbers, your_numbers))
    else:
        print("No match!!")


def part1():
    total = 0
    for card in cards:
        card_number, winning_numbers, your_numbers = card

        number_of_matches = 0

        for number in winning_numbers:
            if number in your_numbers:
                number_of_matches += 1

        score = 0
        while number_of_matches > 0:
            if score == 0:
                score += 1
            else:
                score *= 2
            number_of_matches -= 1

        total += score
    return total 

def part2():
    number_of_cards = 0
    for card in cards:
        total = 1
        cards_stack = [card]
        while len(cards_stack) > 0:
            card = cards_stack.pop()
            card_number, winning_numbers, your_numbers = card

            number_of_matches = 0

            for number in winning_numbers:
                if number in your_numbers:
                    number_of_matches += 1

            total += number_of_matches

            # add the next x (x = number_of_matches) cards to the stack 
            for i in range(number_of_matches):
                cards_stack.append(cards[card_number + i])
        number_of_cards += total
    return number_of_cards


print(part1())
print(part2())
