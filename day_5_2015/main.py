import re

def solve(input_lines, pattern):
    result = 0
    for line in input_lines:
        if re.match(pattern, line) is not None:
            result += 1
    return result

def solve_part_1(input_lines):
    return solve(
        input_lines,
        r"^(?=(.*[aeiou]){3})(?=.*([a-z])\2)(?!.*(ab|cd|pq|xy))",
    )

def solve_part_2(input_lines):
    return solve(input_lines, r"^(?=.*(\w{2}).*\1)(?=.*([a-z])[a-z]\2)")

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
