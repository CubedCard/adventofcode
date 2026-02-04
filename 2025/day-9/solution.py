import sys
import functools
import z3

FILE = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
sys.setrecursionlimit(100000)


def load_lines(filename=FILE):
    with open(filename, encoding="utf-8") as f:
        return [line.strip() for line in f]


def parse_machines(lines):
    machines = []

    for line in lines:
        parts = line.split(" ")
        target = parts[0][1:-1]

        buttons = [
            [int(x) for x in b[1:-1].split(",")]
            for b in parts[1:-1]
            if b.startswith("(")
        ]

        joltage = [int(x) for x in parts[-1][1:-1].split(",")]
        machines.append((target, buttons, joltage))

    return machines


def solve_machine_part1(target, buttons):
    @functools.cache
    def recurse(state, pressed):
        if state == target:
            return 0
        if pressed > len(state):
            return 10**13

        best = 10**13
        for btn in buttons:
            new_state = list(state)
            for i in btn:
                new_state[i] = "#" if new_state[i] == "." else "."
            best = min(best, 1 + recurse("".join(new_state), pressed + 1))
        return best

    return recurse("." * len(target), 0)


def part_one(machines):
    return sum(solve_machine_part1(target, buttons) for target, buttons, _ in machines)


def part_two(machines):
    total = 0
    for _, buttons, joltages in machines:
        bs = [z3.Int(f"b{i}") for i in range(len(buttons))]
        opt = z3.Optimize()

        opt.add(
            [
                z3.Sum(bs[b] for b, btn in enumerate(buttons) if j in btn) == jol
                for j, jol in enumerate(joltages)
            ]
        )
        opt.add([b >= 0 for b in bs])
        opt.minimize(z3.Sum(bs))

        assert opt.check() == z3.sat
        model = opt.model()
        total += sum(model[b].as_long() for b in bs)

    return total


lines = load_lines()
machines = parse_machines(lines)

part1 = part_one(machines)
part2 = part_two(machines)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
