def parse_data():
    return [line.strip() for line in open('data.txt')]

def get_register_value(reg_a, reg_b, reg_c, operand):
    return {
        0: operand,
        1: operand,
        2: operand,
        3: operand,
        4: reg_a,
        5: reg_b,
        6: reg_c,
    }.get(operand, 0)

def part_one():
    data = parse_data()
    reg_a = int(data[0].split(": ")[-1])
    reg_b = int(data[1].split(": ")[-1])
    reg_c = int(data[2].split(": ")[-1])
    instructions = [int(x) for x in data[4].split(": ")[-1].split(",")]
    pc = 0
    output = []

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

if __name__ == "__main__":
    print(f"Part 1: {part_one()}")