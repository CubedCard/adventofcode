from functools import cache

rows = []

for row in open('data.txt'):
    field, tests = row.split(' ')
    tests = tuple(map(int, tests.split(',')))
    rows.append((field, tests))

@cache
def validate_and_count_fields(field, tests):
    if len(tests) == 0:
        return 1 if "#" not in field else 0
    elif field == "" or tests[0] > len(field):
        return 0

    if field[0] == ".":
        return validate_and_count_fields(field[1:], tests)

    elif field[0] == "#":
        size = tests[0]
        if all(field[i] != "." for i in range(size)):
            if len(field) == size:
                return 1 if len(tests) == 1 else 0
            if field[size] != "#":
                return validate_and_count_fields("." + field[size + 1:], tests[1:])
        return 0

    else:
        return validate_and_count_fields("." + field[1:], tests) + validate_and_count_fields("#" + field[1:], tests)

def multiply_fields(field, tests):
    field, tests = field + ("?" + field) * 4, tests * 5
    return validate_and_count_fields(field, tests)

print('Part 1:', sum(validate_and_count_fields(field, tests) for field, tests in rows))
print('Part 2:', sum(multiply_fields(field, tests) for field, tests in rows))
