def solve_part_1(input_lines):
    result = 0
    beams = set([input_lines[0].index("S")])
    for line in input_lines[1:]:
        for beam in beams.copy():
            if line[beam] == "^":
                result += 1
                beams.remove(beam)
                beams.add(beam - 1)
                beams.add(beam + 1)

    return result

def solve_part_2(input_lines):
    result = 1
    beams = {input_lines[0].index("S"): 1}
    for line in input_lines[1:]:
        for beam, count in beams.copy().items():
            if line[beam] == "^":
                result += count
                del beams[beam]
                beams[beam - 1] = count + beams.get(beam - 1, 0)
                beams[beam + 1] = count + beams.get(beam + 1, 0)

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
