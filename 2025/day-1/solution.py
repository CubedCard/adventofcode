instructions = [line.strip() for line in open("data.txt")]


def part_1(start, zeros):
    for ins in instructions:
        rotation = ins[0]
        value = int(ins[1:])
        start = start + value if rotation == "R" else start - value
        if start % 100 == 0:
            zeros += 1
    return zeros


def part_2(start, zeros):
    for i in instructions:
        match i[0]:
            case "L":
                val = int(i[1:])
                full = val // 100
                left = val % 100

                if start != 0 and (start - left) <= 0:
                    zeros += 1

                zeros += full
                start = (start - val) % 100

            case "R":
                val = int(i[1:])
                full = val // 100
                left = val % 100

                if (start + left) >= 100:
                    zeros += 1

                zeros += full
                start = (start + val) % 100

    return zeros


print(f"Part 1: {part_1(50, 0)}")
print(f"Part 2: {part_2(50, 0)}")