import re

def split_line(line):
    return [part for part in re.split(r"\s+", line) if part != ""]

def solve_part_1(input_lines):
    operators = split_line(input_lines[-1])
    results = [1 if operator == "*" else 0 for operator in operators]
    for line in input_lines[:-1]:
        parts = [int(part) for part in split_line(line)]
        for (i, part) in enumerate(parts):
            if operators[i] == "*":
                results[i] *= part
            else:
                results[i] += part

    return sum(results)

def solve_part_2(input_lines):
    matches = re.finditer(r"[+*]\s+", input_lines[-1])
    result = 0
    for match in matches:
        operator = match.group()[0]
        value = 1 if operator == "*" else 0
        for column_index in range(match.start(), match.end()):
            operand = 0
            for line in input_lines[:-1]:
                char = line[column_index]
                if char != " ":
                    operand *= 10
                    operand += int(char)
            if operand == 0:
                continue

            if operator == "*":
                value *= operand
            else:
                value += operand
        result += value

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
