from queue import PriorityQueue
from functools import reduce

def get_distance_squared(a, b):
    a_x, a_y, a_z = a
    b_x, b_y, b_z = b
    return (a_x - b_x)**2 + (a_y - b_y)**2 + (a_z - b_z)**2

def parse_junction_boxes(input_lines):
    junction_boxes = []
    for line in input_lines:
        parts = line.split(",")
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        junction_boxes.append((x, y, z))

    return junction_boxes

def build_ordered_queue(junction_boxes):
    connections_queue = []
    for (i, box) in enumerate(junction_boxes):
        for other in junction_boxes[i+1:]:
            distance = get_distance_squared(box, other)
            connections_queue.append((distance, (box, other)))

    connections_queue.sort(key = lambda element: element[0])
    return connections_queue

def solve_part_1(input_lines, num_connections):
    junction_boxes = parse_junction_boxes(input_lines)
    connections_queue = build_ordered_queue(junction_boxes)
    connections = set(boxes for _, boxes in connections_queue[:num_connections])

    connections_map = dict()
    for a, b in connections:
        connections_map[a] = connections_map.get(a, []) + [b]
        connections_map[b] = connections_map.get(b, []) + [a]

    unused_nodes = set(connections_map.keys())
    circuit_sizes = []
    while len(unused_nodes) > 0:
        circuit = set()
        build_circuit(connections_map, circuit, unused_nodes.pop())
        unused_nodes -= circuit
        circuit_sizes.append(len(circuit))

    circuit_sizes.sort(reverse = True)
    return reduce(lambda a, b: a * b, circuit_sizes[:3], 1)

def build_circuit(connections_map, circuit, root):
    circuit.add(root)
    if root not in connections_map:
        return
    for other in connections_map[root]:
        if other not in circuit:
            build_circuit(connections_map, circuit, other)

def solve_part_2(input_lines):
    junction_boxes = parse_junction_boxes(input_lines)
    connections_queue = build_ordered_queue(junction_boxes)

    circuits = dict()
    for box in junction_boxes:
        circuits[box] = set([box])

    for _, boxes in connections_queue:
        a, b = boxes
        if a in circuits[b]:
            continue
        circuits[a] |= circuits[b]
        if len(circuits[a]) == len(junction_boxes):
            break
        for box in circuits[b]:
            circuits[box] = circuits[a]

    a_x, _, _ = a
    b_x, _, _ = b
    return a_x * b_x

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
    run_and_time("1 (example)", lambda: solve_part_1(lines, 10))
    run_and_time("2 (example)", lambda: solve_part_2(lines))

print()
with open(script_dir / "input_real.txt", "r") as file:
    lines = [line.rstrip("\n") for line in file]
    run_and_time("1 (real)", lambda: solve_part_1(lines, 1000))
    run_and_time("2 (real)", lambda: solve_part_2(lines))

print()
