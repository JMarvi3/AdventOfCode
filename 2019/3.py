from current_puzzle import current_puzzle
import aoc_lib


def sim_wire(wire):
    x = y = 0
    for direction in wire.split(','):
        distance = int(direction[1:])
        match direction[0]:
            case 'R':
                for _ in range(distance):
                    x += 1
                    yield x, y
            case 'L':
                for _ in range(distance):
                    x -= 1
                    yield x, y
            case 'U':
                for _ in range(distance):
                    y -= 1
                    yield x, y
            case 'D':
                for _ in range(distance):
                    y += 1
                    yield x, y


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

wires = input_data.splitlines()
visited = [{pos: i+1 for i, pos in enumerate(sim_wire(wire))} for wire in wires]
crosses = set(visited[0]).intersection(visited[1])
x, y = min(crosses, key=lambda pos: abs(pos[0]) + abs(pos[1]))

puzzle.answer_a = abs(x) + abs(y)
print('Part1:', puzzle.answer_a)

min_steps = min(visited[0][pos] + visited[1][pos] for pos in crosses)

puzzle.answer_b = min_steps
print('Part2:', puzzle.answer_b)
