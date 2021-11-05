from aocd.models import Puzzle
import re

field = [[' ']*50 for i in range(6)]
for line in Puzzle(2016, 8).input_data.splitlines():
    if line[1] == 'e':  # rect
        x, y = list(map(int, re.findall(r'\d+', line)))
        for i in range(y):
            for j in range(x):
                field[i][j] = '#'
    elif line[7] == 'c':  # column
        x, b = list(map(int, re.findall(r'\d+', line)))
        d = 6 - (b % 6)
        old = [row[x] for row in field]
        for i in range(6):
            field[i][x] = old[(d + i) % 6]
    else:  # row
        y, b = list(map(int, re.findall(r'\d+', line)))
        field[y] = field[y][-b:] + field[y][:-b]


print(sum(row.count('#') for row in field))
print('\n'.join(''.join(row) for row in field).replace('#', '*'))
