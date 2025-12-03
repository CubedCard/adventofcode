banks = [line.strip() for line in open("data.txt").read().strip().split("\n")]


def bestSubsequence(bank, k):
    to_remove = len(bank) - k
    stack = []

    for digit in bank:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return "".join(stack[:k])


def part(banks, k=2):
    total = 0
    for bank in banks:
        subseq = bestSubsequence(bank, k)
        total += int(subseq)
    return total


print(f"Part 1: {part(banks.copy())}")
print(f"Part 2: {part(banks.copy(), 12)}")