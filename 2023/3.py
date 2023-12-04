from current_puzzle import current_puzzle
from itertools import product
import regex
import aoc_lib

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

field = dict()
symbols = dict()
for y, row in enumerate(input_data.splitlines()):
    for x, c in enumerate(row):
        if c != '.':
            field[(x,y)] = c
        if c not in '0123456789.':
            symbols[(x, y)] = c
max_x, max_y = x, y
for x, y in symbols.keys():
    del field[(x, y)]

good_numbers = dict()
for x, y in symbols.keys():
    for dx, dy in product(range(-1, 2), range(-1, 2)):
        if dx != 0 or dy != 0:
            cx, cy = x+dx, y+dy
            if (cx, cy) in field:
                good_numbers[(cx, cy)] = field[(cx, cy)]
                # go_left
                l_dx = -1
                while (cx+l_dx, cy) in field:
                    good_numbers[(cx+l_dx, cy)] = field[(cx+l_dx, cy)]
                    l_dx -= 1
                # go right
                l_dx = +1
                while (cx+l_dx, cy) in field:
                    good_numbers[(cx+l_dx, cy)] = field[(cx+l_dx, cy)]
                    l_dx += 1


total = 0
for y in range(max_y+1):
    line = ''
    for x in range(max_x+1):
        line += good_numbers.get((x, y), '.')
    total += sum(map(int, regex.findall(r"\d+", line)))
    print(line)

print(total)

# puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

part2 = 0
for (x, y), c in symbols.items():
    if c != '*':
        continue
    gear_numbers = dict()
    for dx, dy in product(range(-1, 2), range(-1, 2)):
        if dx != 0 or dy != 0:
            cx, cy = x+dx, y+dy
            if (cx, cy) in field:
                gear_numbers[(cx, cy)] = field[(cx, cy)]
                # go_left
                l_dx = -1
                while (cx+l_dx, cy) in field:
                    gear_numbers[(cx+l_dx, cy)] = field[(cx+l_dx, cy)]
                    l_dx -= 1
                # go right
                l_dx = +1
                while (cx+l_dx, cy) in field:
                    gear_numbers[(cx+l_dx, cy)] = field[(cx+l_dx, cy)]
                    l_dx += 1
    numbers = []
    max_x = max_y = 0
    for x, y in gear_numbers.keys():
        max_x = max(x, max_x)
        max_y = max(y, max_y)
    for y in range(max_y+1):
        line = ''
        for x in range(max_x+1):
            line += gear_numbers.get((x, y), '.')
        numbers.extend(map(int, regex.findall('\d+', line)))
    if len(numbers) == 2:
        part2 += numbers[0] * numbers[1]
print(part2)

puzzle.answer_b = part2
print('Part2:', puzzle.answer_b)
