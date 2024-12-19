def can_form_string(s, substrings, memo=None):
    if s == "":
        return True
    if memo is None:
        memo = {}
    if s in memo:
        return memo[s]

    for sub in substrings:
        if s.startswith(sub) and can_form_string(s[len(sub):], substrings, memo):
            memo[s] = True
            return True

    memo[s] = False
    return False


def count_ways_to_form_string(s, substrings, memo=None):
    if s == "":
        return 1
    if memo is None:
        memo = {}
    if s in memo:
        return memo[s]

    total_ways = 0
    for sub in substrings:
        if s.startswith(sub):
            total_ways += count_ways_to_form_string(s[len(sub):], substrings, memo)

    memo[s] = total_ways
    return total_ways

data = [line.strip() for line in open("data.txt")]
substrings = [string for string in data[0].split(", ")]
strings = data[2:]

valid_strings = [s for s in strings if can_form_string(s, substrings)]
print(f"Part 1: {len(valid_strings)}")

total = sum([count_ways_to_form_string(s, substrings) for s in strings])
print("Part 2:", total)