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
    ranges = []
    for range_str in input_lines[0].split(","):
        [minimum, maximum] = range_str.split("-")
        ranges.append((int(minimum), int(maximum)))
    ranges.sort(key=lambda r: r[0])

    invalid_ids = set()
    atom = 1
    while True:
        agg = str(atom) + str(atom)
        range_index = 0

        initial = int(agg)
        while range_index < len(ranges) and initial > ranges[range_index][1]:
            range_index += 1
        if range_index == len(ranges):
            break

        while range_index < len(ranges):
            current = int(agg)
            while range_index < len(ranges) and current > ranges[range_index][1]:
                range_index += 1
            if range_index == len(ranges):
                break
            if current >= ranges[range_index][0]:
                invalid_ids.add(current)
            agg += str(atom)

        atom += 1

    return sum(invalid_ids)

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
