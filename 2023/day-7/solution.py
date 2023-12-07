hands = []

for line in open('data.txt'):
    hand, bet = line.split(' ')
    hands.append((hand, int(bet)))

values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
values_part_2 = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 12, 'K': 13, 'A': 14}

def get_score(hand):
    counts = set()
    for card in hand:
        count = hand.count(card)
        counts.add((int(count), card))
    scores = []
    for count, card in counts:
        if count == 5:
            return 6
        elif count == 4:
            return 5
        scores.append(count)
    if 2 in scores and 3 in scores:
        return 4
    elif 3 in scores:
        return 3
    elif 2 in scores and len(scores) == 3:
        return 2
    elif 2 in scores:
        return 1
    return 0

def get_joker_score(hand):
    max_score = 0
    jokers = hand.count('J')
    if jokers == 0:
        return get_score(hand)
    else:
        for card in values_part_2:
            if card != 'J':
                current_score = get_score(hand.replace('J', card, jokers))
                max_score = max(max_score, current_score)
        return max_score

def part1():
    ordering = []
    for hand, bet in hands:
        score = get_score(hand)
        ordering.append((score, bet, hand))

    ordering.sort(key=lambda x: (x[0], [values[c] for c in x[2]]))

    total_score = 0
    for score, bet, hand in ordering:
        current_score = bet * (ordering.index((score, bet, hand)) + 1)
        total_score += current_score

    return total_score

def part2():
    ordering = []
    for hand, bet in hands:
        score = get_joker_score(hand)
        ordering.append((score, bet, hand))

    ordering.sort(key=lambda x: (x[0], [values_part_2[c] for c in x[2]]))

    total_score = 0
    for score, bet, hand in ordering:
        current_score = bet * (ordering.index((score, bet, hand)) + 1)
        total_score += current_score

    return total_score

print(part1())
print(part2())
