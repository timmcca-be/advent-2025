def solve_part_1(input_lines):
    ranges = []
    lines_iter = iter(input_lines)
    for line in lines_iter:
        if line == "":
            break
        [minimum, maximum] = line.split("-")
        ranges.append((int(minimum), int(maximum)))

    result = 0
    for line in lines_iter:
        value = int(line)
        for minimum, maximum in ranges:
            if value >= minimum and value <= maximum:
                result += 1
                break

    return result

def solve_part_2(input_lines):
    ranges = set()
    for line in input_lines:
        if line == "":
            break
        [minimum_str, maximum_str] = line.split("-")
        minimum = int(minimum_str)
        maximum = int(maximum_str)

        # combine with any overlapping ranges before adding
        for other_range in ranges.copy():
            other_min, other_max = other_range
            if minimum > other_max or maximum < other_min:
                continue
            ranges.remove(other_range)
            minimum = min(minimum, other_min)
            maximum = max(maximum, other_max)

        ranges.add((minimum, maximum))

    result = 0
    for minimum, maximum in ranges:
        result += maximum - minimum + 1

    return result

import time
from pathlib import Path

script_dir = Path(__file__).parent

def run_and_time(part_name, func, lines):
    start_time = time.time()
    answer = func(lines)
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Part {part_name}: {answer} ({runtime:.3f} sec)")

print()
with open(script_dir / "input_example.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (example)", solve_part_1, lines)
    run_and_time("2 (example)", solve_part_2, lines)

print()
with open(script_dir / "input_real.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (real)", solve_part_1, lines)
    run_and_time("2 (real)", solve_part_2, lines)

print()
