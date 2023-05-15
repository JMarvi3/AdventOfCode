from current_puzzle import current_puzzle
import aoc_lib
from intcode import Intcode_VM

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
program = list(map(int, input_data.split(',')))

vm = Intcode_VM(program, [1])
status, outputs = vm.run()
puzzle.answer_a = outputs[-1]
print('Part1:', puzzle.answer_a)

vm = Intcode_VM(program, [5])
status, outputs = vm.run()
puzzle.answer_b = outputs[-1]
print('Part2:', puzzle.answer_b)
