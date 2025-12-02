data = open("data.txt").read().strip().split("\n")
ids = [line.split(",") for line in data]
pairs = [[pair.split("-") for pair in id_pair] for id_pair in ids]


def hasEqualSubstrings(s: str) -> bool:
    n = len(s)
    for size in range(1, n):
        if n % size == 0:
            piece = s[:size]
            if piece * (n // size) == s:
                return True
    return False


def isValidPair1(p):
    if p[0] == "0":
        return False
    mid = len(p) // 2
    if p[:mid] == p[mid:]:
        return False
    return True


def isValidPair2(p):
    if p[0] == "0":
        return False
    if hasEqualSubstrings(p):
        return False
    return True


def part(method):
    sum = 0

    for pair in pairs:
        for p in pair:
            p1, p2 = p
            i1, i2 = int(p1), int(p2)
            for i in range(min(i1, i2), max(i1, i2) + 1):
                if not method(str(i)):
                    sum += i
    return sum


print(part(isValidPair1))
print(part(isValidPair2))