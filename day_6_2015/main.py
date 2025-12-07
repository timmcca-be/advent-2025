import re

def get_overlap(a, b):
    a_start, a_end = a
    b_start, b_end = b

    overlap_start = max(a_start, b_start)
    overlap_end = min(a_end, b_end)

    return (overlap_start, overlap_end) if overlap_end >= overlap_start else None

def get_overlap_2d(a, b):
    a_x, a_y = a
    b_x, b_y = b

    overlap_x = get_overlap(a_x, b_x)
    overlap_y = get_overlap(a_y, b_y)
    if overlap_x is None or overlap_y is None:
        return None

    return overlap_x, overlap_y

def get_sections_not_overlapping(a, b):
    a_start, a_end = a
    b_start, b_end = b

    results = []

    if a_start < b_start:
        results.append((a_start, min(a_end, b_start - 1)))
    if a_end > b_end:
        results.append((max(a_start, b_end + 1), a_end))

    return results

def get_sections_not_overlapping_2d(a, b):
    a_x, a_y = a
    b_x, b_y = b

    results_x = get_sections_not_overlapping(a_x, b_x)
    results_y = get_sections_not_overlapping(a_y, b_y)

    results = []
    for result_x in results_x:
        results.append((result_x, a_y))

    overlap_x = get_overlap(a_x, b_x)
    for result_y in results_y:
        results.append((overlap_x, result_y))

    return results

def turn_off(state, span):
    for on_span in state.copy():
        overlap = get_overlap_2d(on_span, span)
        if overlap is None:
            continue
        state.remove(on_span)
        for subspan in get_sections_not_overlapping_2d(on_span, span):
            state.add(subspan)

def turn_on(state, span):
    turn_off(state, span)
    state.add(span)

def toggle(state, span):
    for on_span in state:
        overlap = get_overlap_2d(span, on_span)
        if overlap is None:
            continue
        state.remove(on_span)
        for subspan in get_sections_not_overlapping_2d(span, on_span):
            toggle(state, subspan)
        state.update(get_sections_not_overlapping_2d(on_span, span))
        return
    state.add(span)

pattern = r"^(?P<command>.*?) (?P<xmin>\d+),(?P<ymin>\d+) through (?P<xmax>\d+),(?P<ymax>\d+)$"

def parse_line(line):
    match = re.match(pattern, line)
    command = match.group("command")
    span = (
        (int(match.group("xmin")), int(match.group("xmax"))),
        (int(match.group("ymin")), int(match.group("ymax")))
    )
    return command, span

def solve_part_1(input_lines):
    state = set()
    for line in input_lines:
        command, span = parse_line(line)
        if command == "turn on":
            turn_on(state, span)
        elif command == "turn off":
            turn_off(state, span)
        elif command == "toggle":
            toggle(state, span)
        else:
            raise ValueError(f"unrecognized command: {command}")

    result = 0
    for span_x, span_y in state:
        span_x_start, span_x_end = span_x
        span_y_start, span_y_end = span_y
        result += (span_y_end - span_y_start + 1) * (span_x_end - span_x_start + 1)

    return result

def solve_part_1_alt(input_lines):
    values = [[0] * 1000 for _ in range(1000)]
    for line in input_lines:
        command, span = parse_line(line)
        span_x, span_y = span
        span_start_x, span_end_x = span_x
        span_start_y, span_end_y = span_y
        for x in range(span_start_x, span_end_x + 1):
            for y in range(span_start_y, span_end_y + 1):
                if command == "turn on":
                    values[y][x] = 1
                elif command == "turn off":
                    values[y][x] = 0
                else:
                    values[y][x] = 1 if values[y][x] == 0 else 1

    return sum(sum(row) for row in values)

def change_value(state, span, diff):
    for on_span, value in state.items():
        overlap = get_overlap_2d(span, on_span)
        if overlap is None:
            continue
        del state[on_span]
        overlap_value = value + diff
        if overlap_value > 0:
            state[overlap] = overlap_value
        for subspan in get_sections_not_overlapping_2d(span, on_span):
            # the issue is that recursively breaking down the span like this
            # explodes the number of spans unmanageably quickly. this issue
            # also affects the "toggle" command in part 1, but not as badly.
            # could mitigate this by adding a step to combine spans periodically,
            # or by making the overlap check smarter than
            # "check each span for overlap individually"
            change_value(state, subspan, diff)
        for new_span in get_sections_not_overlapping_2d(on_span, span):
            state[new_span] = value
        return
    if diff > 0:
        state[span] = diff

def solve_part_2(input_lines):
    state = dict()
    for (i, line) in enumerate(input_lines):
        print(i)
        command, span = parse_line(line)
        if command == "turn on":
            change_value(state, span, 1)
        elif command == "turn off":
            change_value(state, span, -1)
        elif command == "toggle":
            change_value(state, span, 2)
        else:
            raise ValueError(f"unrecognized command: {command}")

    result = 0
    for span, value in state.items():
        span_x, span_y = span
        span_x_start, span_x_end = span_x
        span_y_start, span_y_end = span_y

        result += (span_y_end - span_y_start + 1) * (span_x_end - span_x_start + 1) * value

    return result

diffs = {
    "turn on": 1,
    "turn off": -1,
    "toggle": 2,
}

def solve_part_2_alt(input_lines):
    values = [[0] * 1000 for _ in range(1000)]
    for line in input_lines:
        command, span = parse_line(line)
        diff = diffs[command]
        span_x, span_y = span
        span_start_x, span_end_x = span_x
        span_start_y, span_end_y = span_y
        for x in range(span_start_x, span_end_x + 1):
            for y in range(span_start_y, span_end_y + 1):
                values[y][x] = max(0, values[y][x] + diff)

    return sum(sum(row) for row in values)

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
    run_and_time("2 (example)", solve_part_2_alt, lines)

print()
with open(script_dir / "input_real.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (real)", solve_part_1, lines)
    run_and_time("2 (real)", solve_part_2_alt, lines)

print()
