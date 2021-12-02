from current_puzzle import current_puzzle
import re

pat = re.compile(r"(\w+) (\d+)")
puzzle = current_puzzle()
input_data = puzzle.input_data
inputs = [pat.match(line).groups() for line in input_data.splitlines()]
depth = x = 0
for command, num in inputs:
    num = int(num)
    if command == 'forward':
        x += num
    elif command == 'down':
        depth += num
    elif command == 'up':
        depth -= num

puzzle.answer_a = x * depth
print('Part1:', puzzle.answer_a)

depth = x = aim = 0
for command, num in inputs:
    num = int(num)
    if command == 'forward':
        x += num
        depth += aim * num
    elif command == 'down':
        aim += num
    elif command == 'up':
        aim -= num

puzzle.answer_b = x * depth
print('Part2:', puzzle.answer_b)
