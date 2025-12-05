from functools import reduce

def solve_part_1(input_lines):
    result = 0
    for line in input_lines:
        [length, width, height] = [int(part) for part in line.split("x")]
        sides_area = [length * width, width * height, height * length]
        surface_area = 2 * sum(sides_area)
        slack = min(sides_area)
        result += surface_area + slack
    return result

def solve_part_2(input_lines):
    result = 0
    for line in input_lines:
        dimensions = [int(part) for part in line.split("x")]
        dimensions.sort()
        smallest_perimeter = 2 * (dimensions[0] + dimensions[1])
        volume = reduce(lambda a, b: a * b, dimensions, 1)
        result += smallest_perimeter + volume
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
