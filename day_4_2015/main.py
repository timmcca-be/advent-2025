import hashlib

def solve(prefix, num_zeroes):
    result = 1
    while True:
        md5 = hashlib.md5()
        md5.update(f"{prefix}{result}".encode("utf-8"))
        if md5.hexdigest().startswith("0" * num_zeroes):
            return result
        result += 1


def solve_part_1(input_lines):
    return solve(input_lines[0], 5)

def solve_part_2(input_lines):
    return solve(input_lines[0], 6)

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
