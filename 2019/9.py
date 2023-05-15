from current_puzzle import current_puzzle
import aoc_lib
from intcode import Intcode_VM

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

vm = Intcode_VM(input_data)
status, outputs = vm.run([1])

puzzle.answer_a = outputs[-1]
print('Part1:', puzzle.answer_a)

vm.reset()
status, outputs = vm.run([2])
puzzle.answer_b = outputs[-1]
print('Part2:', puzzle.answer_b)
