total = 0

with open("ex.txt") as f:
    lines = [line.rstrip("\n") for line in f]

number_lines = lines[:-1]
op_line = lines[-1]

columns = list(zip(*[row.split() for row in number_lines]))

ops = op_line.split()

for col_vals, op in zip(columns, ops):
    nums = list(map(int, col_vals))

    if op == "+":
        total += sum(nums)
    elif op == "*":
        prod = 1
        for n in nums:
            prod *= n
        total += prod
    else:
        raise ValueError(f"Unknown operator {op}")

print(total)

