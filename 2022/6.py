from current_puzzle import current_puzzle
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

part1_answer = part2_answer = None
for i in range(len(input_data)):
    if part1_answer is None and i >= 4 and len(set(input_data[i - 4:i])) == 4:
        part1_answer = i
    if part2_answer is None and i >= 14 and len(set(input_data[i - 14:i])) == 14:
        part2_answer = i
    if part1_answer and part2_answer:
        break

puzzle.answer_a = part1_answer
print('Part1:', puzzle.answer_a)
puzzle.answer_b = part2_answer
print('Part2:', puzzle.answer_b)
