import re
from collections import defaultdict

def add_logic_gate_to_circuit(circuit, input_wire1, gate_operator, input_wire2, output_wire):
    circuit.setdefault(input_wire1, []).append((gate_operator, input_wire2, output_wire))
    circuit.setdefault(input_wire2, []).append((gate_operator, input_wire1, output_wire))

def parse_input_data(input_text):
    initial_values = {}
    circuit = defaultdict(list)

    for block in input_text.strip().split("\n\n"):
        for line in block.split("\n"):
            if ":" in line:
                wire, value = line.split(": ")
                initial_values[wire] = int(value)
            elif "->" in line:
                match = re.match(r"(\w+)\s+(AND|OR|XOR)\s+(\w+)\s+->\s+(\w+)", line)
                if match:
                    input_wire1, gate_operator, input_wire2, output_wire = match.groups()
                    add_logic_gate_to_circuit(circuit, input_wire1, gate_operator, input_wire2, output_wire)

    return initial_values, circuit

def simulate_boolean_circuit(initial_values, circuit):
    wire_values = defaultdict(lambda: None)
    wire_values.update(initial_values)

    pending_gates = [(input_wire1, gate_operator, input_wire2, output_wire) for input_wire1 in circuit for gate_operator, input_wire2, output_wire in circuit[input_wire1]]

    def evaluate_gate(input_wire1, gate_operator, input_wire2):
        value1 = wire_values[input_wire1] if input_wire1 in wire_values else None
        value2 = wire_values[input_wire2] if input_wire2 in wire_values else None

        if value1 is None or value2 is None:
            return None

        if gate_operator == "AND":
            return value1 & value2
        elif gate_operator == "OR":
            return value1 | value2
        elif gate_operator == "XOR":
            return value1 ^ value2

    while pending_gates:
        new_pending_gates = []
        for input_wire1, gate_operator, input_wire2, output_wire in pending_gates:
            result = evaluate_gate(input_wire1, gate_operator, input_wire2)
            if result is not None:
                wire_values[output_wire] = result
            else:
                new_pending_gates.append((input_wire1, gate_operator, input_wire2, output_wire))
        pending_gates = new_pending_gates

    return wire_values

def calculate_binary_output(wire_values):
    z_wires = {wire: value for wire, value in wire_values.items() if wire.startswith('z')}

    sorted_bits = [value for wire, value in sorted(z_wires.items(), key=lambda x: -int(x[0][1:]))]

    binary_number = int("".join(map(str, sorted_bits)), 2)
    return binary_number

def identify_swapped_output_wires(circuit):
    swapped = []
    carry_in = None

    for i in range(45):
        wire_index = str(i).zfill(2)
        xor_output, and_output, carry_out, result_wire, z_wire = None, None, None, None, None

        xor_output = next((output_wire for gate_operator, input_wire2, output_wire in circuit[f"x{wire_index}"] if gate_operator == "XOR" and input_wire2 == f"y{wire_index}"), None)
        and_output = next((output_wire for gate_operator, input_wire2, output_wire in circuit[f"x{wire_index}"] if gate_operator == "AND" and input_wire2 == f"y{wire_index}"), None)

        if carry_in:
            carry_out = next((output_wire for gate_operator, input_wire2, output_wire in circuit[carry_in] if gate_operator == "AND" and input_wire2 == xor_output), None)

            if not carry_out:
                xor_output, and_output = and_output, xor_output
                swapped.extend([xor_output, and_output])
                carry_out = next((output_wire for gate_operator, input_wire2, output_wire in circuit[carry_in] if gate_operator == "AND" and input_wire2 == xor_output), None)

            result_wire = next((output_wire for gate_operator, input_wire2, output_wire in circuit[carry_in] if gate_operator == "XOR" and input_wire2 == xor_output), None)

            if xor_output and xor_output.startswith("z"):
                xor_output, result_wire = result_wire, xor_output
                swapped.extend([xor_output, result_wire])

            if and_output and and_output.startswith("z"):
                and_output, result_wire = result_wire, and_output
                swapped.extend([and_output, result_wire])

            if carry_out and carry_out.startswith("z"):
                carry_out, result_wire = result_wire, carry_out
                swapped.extend([carry_out, result_wire])

            z_wire = next((output_wire for gate_operator, input_wire2, output_wire in circuit[carry_out] if gate_operator == "OR" and input_wire2 == and_output), None)

        if z_wire and z_wire.startswith("z") and z_wire != "z45":
            z_wire, result_wire = result_wire, z_wire
            swapped.extend([z_wire, result_wire])

        carry_in = z_wire if carry_in else and_output

    return ",".join(sorted(swapped))

def part_1(initial_values, circuit):
    return calculate_binary_output(simulate_boolean_circuit(initial_values, circuit))

def part_2(circuit):
    return identify_swapped_output_wires(circuit)

if __name__ == "__main__":
    data = open("data.txt").read()

    initial_values, circuit = parse_input_data(data)

    print(f"Part 1: {part_1(initial_values, circuit)}")
    print(f"Part 2: {part_2(circuit)}")