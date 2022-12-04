from current_puzzle import current_puzzle
import parse
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data  = open('4.example').read()

count = 0
part2_count = 0
for line in input_data.split('\n'):
    a, b, c, d = map(int, line.replace('-', ',').split(','))
    # a, b, c, d = parse.parse('{:d}-{:d},{:d}-{:d}', line).fixed
    if (a <= c and d <= b) or (c <= a and b <= d):
        count += 1
    if not ((a < d and c > b) or (c < b and d < a)):
        part2_count += 1

puzzle.answer_a = count
print('Part1:', puzzle.answer_a)
puzzle.answer_b = part2_count
print('Part2:', puzzle.answer_b)
