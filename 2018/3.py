from aocd.models import Puzzle
from parse import compile

pat = compile("#{:d} @ {:d},{:d}: {:d}x{:d}")
claims = list(map(pat.parse, Puzzle(2018, 3).input_data.splitlines()))

fabric = dict()
for _, x, y, w, l in claims:
    for i in range(y, y+l):
        for j in range(x, x+w):
            fabric[(i, j)] = 'X' if (i, j) in fabric else '#'
print('Part1:', list(fabric.values()).count('X'))

for claim, x, y, w, l in claims:
    if not any(fabric[(i, j)] == 'X' for i in range(y, y+l) for j in range(x, x+w)):
        break
print('Part2:', claim)

# intact_claim = next(claim for claim, x, y, w, l in claims if
#                     not any(fabric[(time, j)] == 'X' for time in range(y, y+l) for j in range(x, x+w)))
