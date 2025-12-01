# I totally understand the creator of Advent wanting more free time,
# but I'm a bit bummed about only having 12 puzzles this year (2025)!
# I'm going to do 2015 this year as well, which was before I started
# doing Advent, to stretch the season out a bit.

def solve_part_1(input_lines):
    result = 0
    for character in input_lines[0]:
        result += 1 if character == "(" else -1
    return result

def solve_part_2(input_lines):
    result = 0
    for (i, character) in enumerate(input_lines[0]):
        result += 1 if character == "(" else -1
        if result < 0:
            return i + 1
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
