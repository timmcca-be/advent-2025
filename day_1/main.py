# we're so back baby

def solve_part_1(input_lines):
    result = 0
    position = 50

    for line in input_lines:
        direction = 1 if line[0] == 'R' else -1
        count = int(line[1:])

        position += count * direction
        position %= 100

        if position == 0:
            result += 1

    return result

def solve_part_2(input_lines):
    result = 0
    position = 50

    for line in input_lines:
        direction = 1 if line[0] == 'R' else -1
        count = int(line[1:])
        was_at_zero = position == 0

        position += count * direction

        if position <= 0 and not was_at_zero:
            # we started positive and ended at zero or in the negatives,
            # meaning we touched zero
            result += 1
        # count the times we crossed zero to increase the hundreds digit,
        # regardless of direction
        result += abs(position) // 100

        position %= 100

    return result

# using this to debug my "fancier" solution
def solve_part_2_naive(input_lines):
    result = 0
    position = 50

    for line in input_lines:
        direction = 1 if line[0] == 'R' else -1
        count = int(line[1:])

        for i in range(count):
            position += direction
            position %= 100
            if position == 0:
                result += 1

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
