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
                # originally I had:
                # del beams[beam]
                # but if there's another splitter right next to this one, that
                # could delete the beams that just moved into this column! we
                # need to subtract count, not set the whole column to 0.
                beams[beam] -= count
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
# this input catches a bug in my first version of this, which got the right
# answer on the real input anyway!
lines = """\
...S...
...|...
...^...
..|.|..
..|.^..
..||.|.
..^^.|.
.|||||.
.|^^||.
.|..||.""".split("\n")
run_and_time("1 (test)", solve_part_1, lines)
run_and_time("2 (test)", solve_part_2, lines)

print()
