import operator

def concatenate_numbers(a, b):
    return int(f"{a}{b}")

def evaluate_equations(ops):
    total = 0
    with open('data.txt', 'r') as file:
        for line in file:
            parts = list(map(int, line.replace(':', '').split()))
            target, first, *others = parts

            values = [first]
            for num in others:
                new_values = []
                for val in values:
                    for operation in ops:
                        new_values.append(operation(val, num))
                values = new_values

            if target in values:
                total += target
    return total

if __name__ == '__main__':
    operations_part1 = [operator.add, operator.mul]
    operations_part2 = [operator.add, operator.mul, concatenate_numbers]

    print(f"Part 1: {evaluate_equations(operations_part1)}")
    print(f"Part 2: {evaluate_equations(operations_part2)}")

