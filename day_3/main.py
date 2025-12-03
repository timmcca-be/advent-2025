def clamp(value, minimum, maximum):
    return max(min(value, maximum), minimum)

def solve_line(line, num_batteries):
    result = 0
    for (i, battery_str) in enumerate(line):
        battery = int(battery_str)
        # 1 means ones digit, 2 means tens digit, etc.
        # we can't update more than len(line) - i digits,
        # since we need enough digits to fill up the rest of the number.
        max_digit_to_update = clamp(len(line) - i, 1, num_batteries)
        for digit_number in range(max_digit_to_update, 0, -1):
            # replace the digit at digit_number with battery,
            # and set all digits below to 0.
            # e.g. result is 9753, digit_number is 3, battery is 8 ->
            #      new_result is 9800
            new_result = (
                result -
                (result % (10**digit_number)) +
                battery * 10**(digit_number - 1)
            )
            if new_result > result:
                result = new_result
                break
    return result

def solve(input_lines, num_batteries):
    return sum(solve_line(line, num_batteries) for line in input_lines)

def solve_part_1(input_lines):
    return solve(input_lines, 2)

def solve_part_2(input_lines):
    return solve(input_lines, 12)

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
