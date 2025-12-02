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
    invalid_ids = set()
    for range_str in input_lines[0].split(","):
        [minimum_str, maximum_str] = range_str.split("-")
        minimum = int(minimum_str)
        maximum = int(maximum_str)

        atom = 1
        while int(str(atom) + str(atom)) <= maximum:
            agg = str(atom) + str(atom)
            while True:
                current = int(agg)
                if current > maximum:
                    break
                if current >= minimum:
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
