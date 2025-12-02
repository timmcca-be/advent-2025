import re

def solve_part_1(input_lines):
    result = 0
    for range_str in input_lines[0].split(","):
        [minimum_str, maximum_str] = range_str.split("-")

        min_atom_size = (len(minimum_str) + 1) // 2
        atom = (
            int(minimum_str[:min_atom_size])
            if len(minimum_str) % 2 == 0
            else 10**(min_atom_size - 1)
        )

        minimum = int(minimum_str)
        maximum = int(maximum_str)

        while True:
            invalid_id = int(str(atom) + str(atom))
            atom += 1
            if invalid_id < minimum:
                continue
            if invalid_id > maximum:
                break
            result += invalid_id

    return result

def solve_part_2(input_lines):
    result = 0
    for range_str in input_lines[0].split(","):
        [minimum_str, maximum_str] = range_str.split("-")
        minimum = int(minimum_str)
        maximum = int(maximum_str)

        for i in range(minimum, maximum):
            current_str = str(i)
            for divisor in range(1, len(current_str) // 2 + 1):
                if len(current_str) % divisor != 0:
                    continue

                ref = current_str[:divisor]
                is_valid = True
                for position in range(divisor, len(current_str), divisor):
                    is_valid = (
                        is_valid and
                        current_str[position:position+divisor] == ref
                    )
                    if not is_valid:
                        break

                if is_valid:
                    result += i
                    break

    return result

from pathlib import Path

script_dir = Path(__file__).parent

print()
with open(script_dir / "input_example.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    print("Part 1 (example):", solve_part_1(lines))
    print("Part 2 (example):", solve_part_2(lines))

print()
with open(script_dir / "input_real.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    print("Part 1 (real):", solve_part_1(lines))
    print("Part 2 (real):", solve_part_2(lines))

print()
