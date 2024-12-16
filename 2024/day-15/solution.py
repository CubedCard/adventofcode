initial_grid, instructions = open("data.txt").read().strip().split("\n\n")
commands = [{">": 1, "^": -1j, "<": -1, "v": 1j}[c] for c in instructions.replace("\n", "")]

def simulate_movement(grid, commands, push_enabled):
    grid_map = {c + 1j * r: v for r, row in enumerate(grid.splitlines()) for c, v in enumerate(row.strip())}
    bot_position = next(pos for pos, val in grid_map.items() if val == "@")

    def push(position, command, apply_push):
        target = position + command
        if grid_map.get(target) == "#":
            return False
        elif grid_map.get(target) == ".":
            valid = True
        elif grid_map.get(target) == "O" or command.imag == 0:
            valid = push(target, command, apply_push)
        elif grid_map.get(target) == "[":
            valid = push(target, command, apply_push) and push(position + 1 + command, command, apply_push)
        elif grid_map.get(target) == "]":
            valid = push(target, command, apply_push) and push(position - 1 + command, command, apply_push)

        if apply_push and valid:
            grid_map[position], grid_map[target] = grid_map[target], grid_map[position]
        return valid

    for command in commands:
        if push(bot_position, command, False):
            push(bot_position, command, True)
            bot_position += command

    return int(sum(pos.real + 100 * pos.imag for pos, val in grid_map.items() if val in "[O"))

print(f"Part 1: {simulate_movement(initial_grid, commands, False)}")

updated_grid = initial_grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
print(f"Part 2: {simulate_movement(updated_grid, commands, False)}")