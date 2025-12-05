def move(location, direction):
    x, y = location
    if direction == "^":
        y -= 1
    elif direction == "v":
        y += 1
    elif direction == ">":
        x += 1
    elif direction == "<":
        x -= 1
    else:
        raise ValueError(f"unrecognized direction: {direction}")

    return (x, y)

def solve(directions, num_santas):
    start = (0, 0)
    santas = [start] * num_santas
    visited = set([start])
    for (i, direction) in enumerate(directions):
        santa_index = i % num_santas
        santas[santa_index] = move(santas[santa_index], direction)
        visited.add(santas[santa_index])

    return len(visited)

def solve_part_1(input_lines):
    return solve(input_lines[0], 1)

def solve_part_2(input_lines):
    return solve(input_lines[0], 2)

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
