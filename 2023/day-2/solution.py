games = []

for game in open('data.txt'):
    game_info = game.split(':')

    game_number = int(game_info[0].strip().replace("Game", "").strip())

    rounds = []
    for round_str in game_info[1].split(';'):
        turns = [turn.strip().split() for turn in round_str.strip().split(',')]
        round_data = [(int(num), color) for num, color in turns]
        rounds.append(round_data)

    result_tuple = (game_number, rounds)

    games.append(result_tuple)


def part1():
    not_valid_game_ids = []
    for game in games:
        for round in game[1]:
            red_count = 0
            green_count = 0
            blue_count = 0
            for turn in round:
                if turn[1] == 'red':
                    red_count += turn[0]
                elif turn[1] == 'green':
                    green_count += turn[0]
                elif turn[1] == 'blue':
                    blue_count += turn[0]

            if red_count > 12 or green_count > 13 or blue_count > 14:
                not_valid_game_ids.append(game[0])
                break

    sum_valid = 0
    for game in games:
        if game[0] not in not_valid_game_ids:
            sum_valid += game[0]

    return sum_valid

def part2():
    total_powers = 0
    for game in games:
        max_red_count = 1
        max_green_count = 1
        max_blue_count = 1
        for round in game[1]:
            for turn in round:
                if turn[1] == 'red':
                    max_red_count = max(max_red_count, turn[0])
                elif turn[1] == 'green':
                    max_green_count = max(max_green_count, turn[0])
                elif turn[1] == 'blue':
                    max_blue_count = max(max_blue_count, turn[0])
        power = max_red_count * max_green_count * max_blue_count
        total_powers += power

    return total_powers

print(part1())
print(part2())
