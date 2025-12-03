banks = [line.strip() for line in open("data.txt").read().strip().split("\n")]


def part1(banks):
    max_pairs = []
    for bank in banks:
        highest = -1
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                pair = int(bank[i] + bank[j])
                if pair > highest:
                    highest = pair
        max_pairs.append(highest)
    return sum(max_pairs)


def bestSubsequence(bank, k):
    to_remove = len(bank) - k
    stack = []

    for digit in bank:
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)

    return "".join(stack[:k])


def part2(banks, k=12):
    total = 0
    for bank in banks:
        subseq = bestSubsequence(bank, k)
        total += int(subseq)
    return total


print("Part 1:", part1(banks.copy()))
print("Part 2:", part2(banks.copy()))