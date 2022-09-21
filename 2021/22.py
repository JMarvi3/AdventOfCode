from current_puzzle import current_puzzle
import re
import numpy as np
import time
from joblib import Parallel, delayed

start = time.perf_counter()
puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('22_2.example').read()

cells = np.zeros((200, 200, 200), dtype=bool)
def restrict(n): return max(-50, min(n, 50)) + 100


steps = []
X, Y, Z = [], [], []
for line in input_data.splitlines():
    command, x0, x1, y0, y1, z0, z1 = line[:2], *map(int, re.findall(r"-?\d+", line))
    x1 += 1
    y1 += 1
    z1 += 1
    cells[restrict(x0):restrict(x1), restrict(y0):restrict(y1), restrict(z0):restrict(z1)] = command == "on"
    X.extend((x0, x1))
    Y.extend((y0, y1))
    Z.extend((z0, z1))
    steps.append((command, x0, x1, y0, y1, z0, z1))

total = cells.sum()
print(f"Part 1: {total}")
puzzle.answer_a = total

X.sort()
Y.sort()
Z.sort()
N = len(X)
cells = np.zeros((N, N, N), dtype=bool)

for step in steps:
    x0 = X.index(step[1])
    x1 = X.index(step[2])
    y0 = Y.index(step[3])
    y1 = Y.index(step[4])
    z0 = Z.index(step[5])
    z1 = Z.index(step[6])
    cells[x0:x1, y0:y1, z0:z1] = step[0] == "on"


def calc_x(x, work_cells):
    on = 0
    x_range = (X[x + 1] - X[x])
    for y in range(N - 1):
        y_range = (Y[y + 1] - Y[y]) * x_range
        on += sum(int(work_cells[y][z]) * y_range * (Z[z + 1] - Z[z]) for z in range(N - 1))
    return on


print('Calculating Part 2: ', end='')
on_cells = sum(Parallel(n_jobs=16)(delayed(calc_x)(x, cells[x]) for x in range(N - 1)))
print(on_cells)
print(f"Time spent: {time.perf_counter() - start:.2f}s")
puzzle.answer_b = on_cells
