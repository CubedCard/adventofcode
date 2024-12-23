def process_number(x):
    modulo = 16777216

    result = x * 64
    x ^= result
    x %= modulo

    result = x // 32
    x ^= result
    x %= modulo

    result = x * 2048
    x ^= result
    x %= modulo

    return x

def generate_sequence_and_diff(x, length):
    sequence = []
    differences = []

    for _ in range(length):
        current_digit = x % 10
        x = process_number(x)
        next_digit = x % 10

        sequence.append(next_digit)
        differences.append(next_digit - current_digit)

    return x, sequence, convert_to_string(differences)

def convert_to_string(differences):
    return "".join([chr(i + ord('m')) for i in differences])

def calculate_pattern_scores(data, sequence_length):
    pattern_scores = {}

    for x in data:
        _, sequence, differences = generate_sequence_and_diff(x, sequence_length)
        seen_patterns = set()

        for i in range(len(differences) - 3):
            pattern = tuple(differences[i:i + 4])
            next_point = sequence[i + 3]

            if pattern not in seen_patterns:
                seen_patterns.add(pattern)
                if pattern not in pattern_scores:
                    pattern_scores[pattern] = 0
                pattern_scores[pattern] += next_point

    return pattern_scores

def part_1(data):
    total = 0
    for num in data:
        cur = int(num)
        for _ in range(2000):
            cur = process_number(cur)
        total += cur
    return total

if __name__ == "__main__":
    data = [int(line.strip()) for line in open('data.txt')]

    pattern_scores = calculate_pattern_scores(data, 2000)
    max_score = max(pattern_scores.values())

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {max_score}")