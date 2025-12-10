def solve_part_1(input_lines):
    top_left_candidates = []
    top_right_candidates = []
    bottom_left_candidates = []
    bottom_right_candidates = []
    for line in input_lines:
        parts = line.split(",")
        element = (int(parts[0]), int(parts[1]))
        top_left_candidates = update_corner_candidates(
            top_left_candidates, element, TOP_LEFT)
        top_right_candidates = update_corner_candidates(
            top_right_candidates, element, TOP_RIGHT)
        bottom_left_candidates = update_corner_candidates(
            bottom_left_candidates, element, BOTTOM_LEFT)
        bottom_right_candidates = update_corner_candidates(
            bottom_right_candidates, element, BOTTOM_RIGHT)

    result = 0
    for top_left in top_left_candidates:
        for bottom_right in bottom_right_candidates:
            result = max(result, area(top_left, bottom_right))
    for top_right in top_right_candidates:
        for bottom_left in bottom_left_candidates:
            result = max(result, area(top_right, bottom_left))

    return result

TOP_LEFT = (-1, -1)
TOP_RIGHT = (1, -1)
BOTTOM_LEFT = (-1, 1)
BOTTOM_RIGHT = (1, 1)

def is_strictly_better(element, ref, direction):
    el_x, el_y = element
    ref_x, ref_y = ref
    dir_x, dir_y = direction
    return el_x * dir_x >= ref_x * dir_x and el_y * dir_y >= ref_y * dir_y

def update_corner_candidates(candidates, element, direction):
    result = [
        candidate for candidate in candidates
        if not is_strictly_better(element, candidate, direction)
    ]
    if not any(
        is_strictly_better(candidate, element, direction)
        for candidate in result
    ):
        result.append(element)
    return result

def area(a, b):
    a_x, a_y = a
    b_x, b_y = b
    return (abs(a_x - b_x) + 1) * (abs(a_y - b_y) + 1)

def solve_part_2(input_lines):
    elements = []
    for line in input_lines:
        parts = line.split(",")
        elements.append((int(parts[0]), int(parts[1])))

    top_element_index = min_index(elements, lambda el: el[1])

    boundaries = [
        make_boundary(elements[i], elements[(i + 1) % len(elements)])
        for i in range(len(elements))
    ]
    definite_top_boundary_index = (
        top_element_index
        if is_horizontal(boundaries[top_element_index])
        else (top_element_index - 1) % len(elements)
    )
    boundary_directions = [None] * len(boundaries)
    boundary_directions[definite_top_boundary_index] = -1
    for i in range(1, len(boundaries)):
        current_index = (definite_top_boundary_index + i) % len(boundaries)
        prev_index = (current_index - 1) % len(boundaries)
        current_boundary = boundaries[current_index]
        prev_boundary = boundaries[prev_index]
        prev_direction = boundary_directions[prev_index]

        if current_boundary[0] == prev_boundary[0] or current_boundary[1] == prev_boundary[1]:
            # top left or bottom right corner
            direction = prev_direction
        else:
            # top right or bottom left corner
            direction = -prev_direction

        boundary_directions[current_index] = direction

    adjusted_coordinates = []
    for (i, boundary) in enumerate(boundaries):
        a, b = boundary
        a_x, a_y = a
        directed_offset = 0.5 * boundary_directions[i]
        if is_horizontal(boundary):
            adjusted_coordinates.append(a_y + directed_offset)
        else:
            adjusted_coordinates.append(a_x + directed_offset)

    y_first = is_horizontal(boundaries[0])
    adjusted_corners = []
    for i in range(0, len(adjusted_coordinates), 2):
        current = adjusted_coordinates[i]
        prev = adjusted_coordinates[(i - 1) % len(adjusted_coordinates)]
        next = adjusted_coordinates[i + 1]
        if y_first:
            adjusted_corners.append((prev, current))
            adjusted_corners.append((next, current))
        else:
            adjusted_corners.append((current, prev))
            adjusted_corners.append((current, next))

    adjusted_boundaries = []
    for (i, corner) in enumerate(adjusted_corners):
        adjusted_boundaries.append(make_boundary(
            corner,
            adjusted_corners[(i + 1) % len(adjusted_corners)]
        ))

    max_area = 0
    for (i, a) in enumerate(elements):
        for b in elements[i+1:]:
            if does_path_cross_lines(adjusted_boundaries, a, b):
                continue
            new_area = area(a, b)
            if new_area > max_area:
                max_area = new_area

    return max_area

def make_boundary(a, b):
    a_x, a_y = a
    b_x, b_y = b
    # boundaries are always from the top left toward the bottom right.
    # since they're always vertical or horizontal, that check is pretty simple.
    return (a, b) if a_x < b_x or a_y < b_y else (b, a)

def min_index(elements, key):
    result = 0
    lowest_key = key(elements[0])
    for i in range(1, len(elements)):
        element_key = key(elements[i])
        if element_key < lowest_key:
            lowest_key = element_key
            result = i

    return result

def is_horizontal(line):
    a, b = line
    return a[1] == b[1]

def do_lines_cross(line, ref):
    line_start, line_end = line
    ref_start, ref_end = ref

    line_start_x, line_start_y = line_start
    line_end_x, line_end_y = line_end
    ref_start_x, ref_start_y = ref_start
    ref_end_x, ref_end_y = ref_end

    is_line_horizontal = line_start_y == line_end_y
    is_ref_horizontal = ref_start_y == ref_end_y

    if is_line_horizontal and not is_ref_horizontal:
        return (
            ref_start_y < line_start_y < ref_end_y and
            line_start_x < ref_start_x < line_end_x
        )

    if not is_line_horizontal and is_ref_horizontal:
        return (
            line_start_y < ref_start_y < line_end_y and
            ref_start_x < line_start_x < ref_end_x
        )

    return False

def does_path_cross_lines(adjusted_boundaries, start, end):
    start_x, start_y = start
    end_x, end_y = end
    min_x, max_x = (start_x, end_x) if start_x < end_x else (end_x, start_x)
    min_y, max_y = (start_y, end_y) if start_y < end_y else (end_y, start_y)
    lines = [
        ((min_x, min_y), (min_x, max_y)),
        ((min_x, min_y), (max_x, min_y)),
        ((min_x, max_y), (max_x, max_y)),
        ((max_x, min_y), (max_x, max_y)),
    ]
    return any(
        do_lines_cross(line, ref)
        for line in lines
        for ref in adjusted_boundaries
    )

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
