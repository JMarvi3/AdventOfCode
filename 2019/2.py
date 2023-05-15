from current_puzzle import current_puzzle
import aoc_lib
from intcode import Intcode_VM


def part2(program):
    for noun in range(100):
        for verb in range(100):
            program[1], program[2] = noun, verb
            vm = Intcode_VM(program)
            vm.run()
            result = vm.memory[0]
            if result == 19690720:
                return noun, verb


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

program = list(map(int, input_data.split(',')))
program[1:3] = 12, 2
vm = Intcode_VM(program)
vm.run()
puzzle.answer_a = vm.memory[0]
print('Part1:', puzzle.answer_a)


noun, verb = part2(program)
puzzle.answer_b = 100 * noun + verb
print('Part2:', puzzle.answer_b)
