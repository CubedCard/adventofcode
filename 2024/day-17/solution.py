def parse_data():
    return [line.strip() for line in open('data.txt')]

def get_register_value(reg_a, reg_b, reg_c, operand):
    return { 0: operand, 1: operand, 2: operand, 3: operand, 4: reg_a, 5: reg_b, 6: reg_c, }.get(operand, 0)

def part_one():
    data = parse_data()
    reg_a, reg_b, reg_c = int(data[0].split(": ")[-1]), int(data[1].split(": ")[-1]), int(data[2].split(": ")[-1])
    instructions = [int(x) for x in data[4].split(": ")[-1].split(",")]
    pc, output = 0, []

    while pc < len(instructions):
        opcode, operand = instructions[pc], instructions[pc + 1]
        resolved = get_register_value(reg_a, reg_b, reg_c, operand)

        match opcode:
            case 0:
                reg_a //= 2 ** resolved
            case 1:
                reg_b ^= operand
            case 2:
                reg_b = resolved % 8
            case 3:
                if reg_a != 0:
                    pc = operand
                    continue
            case 4:
                reg_b ^= reg_c
            case 5:
                output.append(str(resolved % 8))
            case 6:
                reg_b = reg_a // 2 ** resolved
            case 7:
                reg_c = reg_a // 2 ** resolved

        pc += 2

    return ",".join(output)

def part_two():
    instructions = [int(x) for x in parse_data()[4].split(": ")[-1].split(",")]

    def compute_output(a):
        return (((a // (2**((a % 8) ^3))) ^ 6) ^ (a % 8)) % 8

    possible = [0]
    for instruction in reversed(instructions):
        new_possible = [num for c in possible for j in range(8) if compute_output((num := (c << 3) + j)) == instruction]
        possible = new_possible

    return min(possible)

if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
