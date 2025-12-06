from typing import List

def read_worksheet(file_path: str) -> List[str]:
    with open(file_path, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]
    return lines

def split_problems(lines: List[str]) -> List[List[str]]:
    num_rows = len(lines)
    num_cols = max(len(line) for line in lines)
    lines = [line.ljust(num_cols) for line in lines]
    
    problems = []
    col = 0
    while col < num_cols:
        if all(lines[row][col] == ' ' for row in range(num_rows)):
            col += 1
            continue
        problem_cols = []
        while col < num_cols and not all(lines[row][col] == ' ' for row in range(num_rows)):
            problem_cols.append(col)
            col += 1
        problems.append(problem_cols)
    return problems

def extract_numbers(lines: List[str], cols: List[int]) -> List[int]:
    num_rows = len(lines)
    number_rows = lines[:-1]
    numbers = []
    for col in cols:
        digits = ''.join(number_rows[row][col] for row in range(num_rows-1)).strip()
        if digits:
            numbers.append(int(digits))
    return numbers

def extract_operator(lines: List[str], cols: List[int]) -> str:
    op_row = lines[-1]
    for col in cols:
        if op_row[col] in '+*':
            return op_row[col]
    return '+'

def compute_problem(numbers: List[int], operator: str) -> int:
    if operator == '+':
        result = sum(numbers)
    elif operator == '*':
        result = 1
        for n in numbers:
            result *= n
    else:
        raise ValueError(f"Unknown operator: {operator}")
    return result

def solve_part2(file_path: str) -> int:
    lines = read_worksheet(file_path)
    lines = [line[::-1] for line in lines]
    problems = split_problems(lines)
    total = 0
    for cols in problems:
        numbers = extract_numbers(lines, cols)
        operator = extract_operator(lines, cols)
        total += compute_problem(numbers, operator)
    return total

if __name__ == "__main__":
    file_path = "data.txt"
    print("Part 2:", solve_part2(file_path))
