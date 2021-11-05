from aocd.models import Puzzle
from collections import defaultdict

data = int(Puzzle(2017, 3).input_data)

s = x = y = 0
for _ in range(data - 1):
    if x == s and y == -s:
        s += 1
        x += 1
    elif y == -s:
        x += 1
    elif x == -s:
        y -= 1
    elif y == s:
        x -= 1
    else:  # x==s
        y += 1

print('Part1:', abs(x) + abs(y))

cells = defaultdict(int)

cells[(0, 0)] = 1
s = x = y = 0
c = 0
while c < data:
    if x == s and y == -s:
        s += 1
        x += 1
    elif y == -s:
        x += 1
    elif x == -s:
        y -= 1
    elif y == s:
        x -= 1
    else:  # x==s
        y += 1
    c = sum(cells[(x + i, y + j)] for i in range(-1, 2) for j in range(-1, 2))
    cells[(x, y)] = c

print('Part2:',c)
