def analyze_string(s, substrings, memo=None):
    if s == "":
        return (True, 1)
    if memo is None:
        memo = {}
    if s in memo:
        return memo[s]

    can_form = False
    total_ways = 0

    for sub in substrings:
        if s.startswith(sub):
            sub_can_form, sub_ways = analyze_string(s[len(sub):], substrings, memo)
            if sub_can_form:
                can_form = True
            total_ways += sub_ways

    memo[s] = (can_form, total_ways)
    return memo[s]

data = [line.strip() for line in open("data.txt")]
substrings = [string for string in data[0].split(", ")]
strings = data[2:]

valid_strings = 0
total = 0

for s in strings:
    can_form, ways = analyze_string(s, substrings)
    if can_form:
        valid_strings += 1
    total += ways

print(f"Part 1: {valid_strings}")
print(f"Part 2: {total}")
