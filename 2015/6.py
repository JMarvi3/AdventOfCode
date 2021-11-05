import re
from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

pat = re.compile(r'([^\d]*) (\d*),(\d*) through (\d*),(\d*)')
lights = set()
for ins in input_data.splitlines():
    m = pat.match(ins)
    if m.group(1) == 'turn on':
        for x in range(int(m.group(2)), int(m.group(4))+1):
            for y in range(int(m.group(3)), int(m.group(5)) + 1):
                lights.add((x, y))
    elif m.group(1) == 'turn off':
        for x in range(int(m.group(2)), int(m.group(4))+1):
            for y in range(int(m.group(3)), int(m.group(5)) + 1):
                if (x, y) in lights:
                    lights.remove((x, y))
    elif m.group(1) == 'toggle':
        for x in range(int(m.group(2)), int(m.group(4))+1):
            for y in range(int(m.group(3)), int(m.group(5)) + 1):
                coord = (x, y)
                if coord in lights:
                    lights.remove(coord)
                else:
                    lights.add(coord)

puzzle.answer_a = len(lights)
print('Part1:', puzzle.answer_a)

lights = [[0]*1000 for i in range(1000)]
diff = 0
for ins in input_data.splitlines():
    m = pat.match(ins)
    if m.group(1) == 'turn on':
        diff = 1
    elif m.group(1) == 'turn off':
        diff = -1
    elif m.group(1) == 'toggle':
        diff = 2

    for x in range(int(m.group(2)), int(m.group(4)) + 1):
        for y in range(int(m.group(3)), int(m.group(5)) + 1):
            lights[x][y] = max(0, lights[x][y] + diff)

puzzle.answer_b = sum(sum(row) for row in lights)
print('Part2:', puzzle.answer_b)
