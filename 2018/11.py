from current_puzzle import current_puzzle
from copy import deepcopy


def get_sum(sums, x, y, size):
    return sums[y+size-1][x+size-1] - sums[y+size-1][x-1] - sums[y-1][x+size-1] + sums[y-1][x-1]


puzzle = current_puzzle()
input_data = puzzle.input_data
serial = int(input_data)
#serial = 42

grid = [[0] * 301 for _ in range(301)]
for y in range(1, 301):
    for x in range(1, 301):
        rack_id = x + 10
        grid[y][x] = (((rack_id * y) + serial) * rack_id) // 100 % 10 - 5

sums = deepcopy(grid)
for x in range(301):
    for y in range(1, 301):
        sums[y][x] = grid[y][x] + sums[y-1][x]

for x in range(1, 301):
    for y in range(1, 301):
        sums[y][x] += sums[y][x-1]

# for x in range(1, 301):
#     for y in range(1, 301):
#         sums[y][x] += sums[y-1][x] + sums[y][x-1]

max_total, max_x, max_y = -float('inf'), 0, 0
for y in range(1, 301-2):
    for x in range(1, 301-2):
        total = get_sum(sums, x, y, 3)
        if total > max_total:
            max_total, max_x, max_y = total, x, y

# print(max_x, max_y, max_total)
puzzle.answer_a = f"{max_x},{max_y}"
print(puzzle.answer_a)

max_total, max_x, max_y, max_size = -float('inf'), 0, 0, 0
for size in range(301):
    for y in range(1, 301-size+1):
        for x in range(1, 301-size+1):
            total = get_sum(sums, x, y, size)
            if total > max_total:
                max_total, max_x, max_y, max_size = total, x, y, size

# print(max_total, max_x, max_y, max_size)
puzzle.answer_b = f"{max_x},{max_y},{max_size}"
print(puzzle.answer_b)
