def solve_part_1(input_lines):
    locations = set()
    for (y, line) in enumerate(input_lines):
        for (x, character) in enumerate(line):
            if character == "@":
                locations.add((x, y))

    result = 0
    for location in locations:
        x, y = location
        neighbors = set(
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ) - set([location])
        neighboring_rolls = neighbors & locations
        if len(neighboring_rolls) < 4:
            result += 1

    return result

def solve_part_2(input_lines):
    locations = set()
    for (y, line) in enumerate(input_lines):
        for (x, character) in enumerate(line):
            if character == "@":
                locations.add((x, y))

    connections = dict()
    for location in locations:
        x, y = location
        neighbors = set(
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ) - set([location])
        connections[location] = neighbors & locations

    removed_locations = set()
    while True:
        did_remove_any = False
        for location in (locations - removed_locations):
            remaining_connections = connections[location] - removed_locations
            if len(remaining_connections) < 4:
                removed_locations.add(location)
                did_remove_any = True
        if not did_remove_any:
            break

    return len(removed_locations)

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
