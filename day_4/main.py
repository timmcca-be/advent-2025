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

    queue = []
    connections = dict()
    for location in locations:
        x, y = location
        neighbors = set(
            (x + dx, y + dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
        ) - set([location])
        neighboring_rolls = neighbors & locations
        connections[location] = neighboring_rolls

        if len(neighboring_rolls) < 4:
            queue.append(location)

    removed_locations = set(queue)
    while len(queue) > 0:
        location = queue.pop()
        for neighbor in connections[location] - removed_locations:
            if len(connections[neighbor] - removed_locations) < 4:
                removed_locations.add(neighbor)
                queue.append(neighbor)

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
