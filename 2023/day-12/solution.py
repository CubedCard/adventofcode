import re
from functools import cache

rows = []

for row in open('data.txt'):
    field, test = row.split(' ')
    rows.append((field, [int(x) for x in test.split(',')]))

def validate_and_count_fields(input_str, tests):
    def is_valid_test(field):
        groups = [len(match.group()) for match in re.finditer(r'#+', field)]
        return groups == tests

    @cache
    def generate_strings(input_str, index=0, current_str=""):
        if index == len(input_str):
            return [current_str]

        if input_str[index] == '?':
            return (
                generate_strings(input_str, index + 1, current_str + '#')
                + generate_strings(input_str, index + 1, current_str + '?')
            )
        else:
            return generate_strings(input_str, index + 1, current_str + input_str[index])

    count_valid = sum(is_valid_test(field) for field in generate_strings(input_str))
    return count_valid

def multiply_fields(field, tests):
    field, tests = field + ("?" + field) * 4, tests * 5
    print(field, tests)
    return validate_and_count_fields(field, tests)

print('Part 1:', sum(validate_and_count_fields(field, tests) for field, tests in rows))
print('Part 2:', sum(multiply_fields(field, tests) for field, tests in rows))
