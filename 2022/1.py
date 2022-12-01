from current_puzzle import current_puzzle
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

elves = []
for group in input_data.split('\n\n'):
    elves.append(sum(aoc_lib.findall('{:d}', group)))

elves.sort()
puzzle.answer_a = elves[-1]
print('Part1:', puzzle.answer_a)
puzzle.answer_b = sum(elves[-3:])
print('Part2:', puzzle.answer_b)
