from current_puzzle import current_puzzle
import re


def calc_size(all_points):
    x, y = zip(*all_points)
    return max(x) - min(x) + max(y) - min(y)


def draw(all_points):
    x, y = zip(*all_points)
    for j in range(min(y), max(y)+1):
        for i in range(min(x), max(x)+1):
            print('#' if (i, j) in all_points else ' ', end='')
        print()


puzzle = current_puzzle()
input_data = puzzle.input_data
pat = re.compile(r"-?\d+")

points = [list(map(int, pat.findall(line))) for line in input_data.splitlines()]

min_time, min_size, min_points = 0, float('inf'), []
time = 0
while True:
    curr_points = list((x + time * dx, y + time * dy) for x, y, dx, dy in points)
    size = calc_size(curr_points)
    if size < min_size:
        min_time, min_size, min_points = time, size, curr_points
    elif size > min_size:
        break
    time += 1

draw(min_points)

puzzle.answer_a = 'BHPJGLPE'
print(puzzle.answer_a)

puzzle.answer_b = min_time
print(puzzle.answer_b)
