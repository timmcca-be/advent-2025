import re

set_pattern = r"^(?P<input>\S+) -> (?P<output>[a-z]+)$"
not_pattern = r"^NOT (?P<input>\S+) -> (?P<output>[a-z]+)$"
operator_pattern = (
    r"^(?P<input1>\S+) (?P<operator>[A-Z]+) (?P<input2>\S+)"
    + r" -> (?P<output>[a-z]+)"
)

def get_value(wires, value):
    if value in wires:
        result = wires[value]
        if isinstance(result, int):
            return result
        output = result(wires)
        wires[value] = output
        return output
    return int(value)

def handle_operator(operator, input1, input2):
    if operator == "AND":
        return input1 & input2
    if operator == "OR":
        return input1 | input2
    if operator == "LSHIFT":
        return input1 << input2
    if operator == "RSHIFT":
        return input1 >> input2
    raise ValueError(f"unrecognized operator: {operator}")

def build_set_wire(input_value):
    return lambda wires: get_value(wires, input_value)

def build_not_wire(input_value):
    return lambda wires: 65535 ^ get_value(wires, input_value)

def build_operator_wire(operator, input1, input2):
    return lambda wires: handle_operator(
        operator,
        get_value(wires, input1),
        get_value(wires, input2),
    )

def build_wires_dict(input_lines):
    wires = dict()
    for line in input_lines:
        match = re.match(set_pattern, line)
        if match is not None:
            wires[match.group("output")] = build_set_wire(match.group("input"))
            continue
        match = re.match(not_pattern, line)
        if match is not None:
            wires[match.group("output")] = build_not_wire(match.group("input"))
            continue
        match = re.match(operator_pattern, line)
        if match is not None:
            wires[match.group("output")] = build_operator_wire(
                match.group("operator"),
                match.group("input1"),
                match.group("input2"),
            )
            continue
        raise ValueError(f"invalid line: {line}")

    return wires

def solve_part_1(input_lines, output_wire):
    wires = build_wires_dict(input_lines)
    return get_value(wires, output_wire)

def solve_part_2(input_lines, a_wire, b_wire):
    wires = build_wires_dict(input_lines)
    wires[b_wire] = get_value(wires.copy(), a_wire)
    return get_value(wires, a_wire)

import time
from pathlib import Path

script_dir = Path(__file__).parent

def run_and_time(part_name, func):
    start_time = time.time()
    answer = func()
    end_time = time.time()
    runtime = end_time - start_time
    print(f"Part {part_name}: {answer} ({runtime:.3f} sec)")

print()
with open(script_dir / "input_example.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (example)", lambda: solve_part_1(lines, "f"))
    run_and_time("2 (example)", lambda: solve_part_2(lines, "f", "x"))

print()
with open(script_dir / "input_real.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (real)", lambda: solve_part_1(lines, "a"))
    run_and_time("2 (real)", lambda: solve_part_2(lines, "a", "b"))

print()
