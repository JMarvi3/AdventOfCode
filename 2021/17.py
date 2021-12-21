from current_puzzle import current_puzzle
import re

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = "target area: x=20..30, y=-10..-5"

min_x, max_x, min_y, max_y = map(int, re.findall(r"-?\d+", input_data))

best = 0
count = 0
for xv_init in range(max_x+1):
    for yv_init in range(min_y-1, 1000):
        x = y = best_y = 0
        xv, yv = xv_init, yv_init
        while True:
            x, xv = x + xv, max(0, xv-1)
            y, yv = y + yv, yv - 1
            best_y = max(best_y, y)
            if min_x <= x <= max_x and min_y <= y <= max_y:
                count += 1
                best = max(best, best_y)
                break
            if x > max_x or y < min_y:
                break

print(best, count)
puzzle.answer_a = best
print('Part1:', puzzle.answer_a)

# print(count)
puzzle.answer_b = count
print('Part2:', puzzle.answer_b)
