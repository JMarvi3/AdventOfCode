from current_puzzle import current_puzzle
from collections import defaultdict


def neighbors(lights, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                count += lights[(x + i, y + j)]
    return count


def lights_iter(lights, part2=False):
    new_lights = lights.copy()
    for x in range(size):
        for y in range(size):
            count = neighbors(lights, x, y)
            if lights[(x, y)]:
                if count != 2 and count != 3:
                    new_lights[(x, y)] = 0
            elif count == 3:
                new_lights[(x, y)] = 1
    if part2:
        for pos in stuck:
            new_lights[pos] = 1
    return new_lights

puzzle = current_puzzle()
input_data = puzzle.input_data

lights = defaultdict(int)
size = 0
for y, line in enumerate(input_data.splitlines()):
    for x, c in enumerate(line.strip()):
        if c == '#':
            lights[(x, y)] = 1
    size = y

size += 1
stuck = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]

part2_lights = lights.copy()
for pos in stuck:
    part2_lights[pos] = 1

for i in range(100):
    part2_lights = lights_iter(part2_lights, part2=True)
    lights = lights_iter(lights)

puzzle.answer_a = sum(lights.values())
print('Part1:', puzzle.answer_a)
puzzle.answer_b = sum(part2_lights.values())
print('Part2:', puzzle.answer_b)
