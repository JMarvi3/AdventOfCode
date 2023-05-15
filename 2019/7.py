from current_puzzle import current_puzzle
import aoc_lib
from intcode import Intcode_VM
import itertools


def try_perm(vm, phases):
    input_value = 0
    for i in range(5):
        vm.reset([phases[i], input_value])
        status, outputs = vm.run()
        input_value = outputs[-1]
    return outputs[-1]


def try_perm_part2(program, phases):
    vms = [Intcode_VM(program, [phases[i]]) for i in range(5)]
    status = None
    prev_output = [0]
    while status != Intcode_VM.DONE:
        for i in range(5):
            status, outputs = vms[i].run(prev_output)
            prev_output = outputs
    return outputs[-1]


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

program = list(map(int, input_data.split(',')))
vm = Intcode_VM(program)
max_thruster = max(try_perm(vm, perm) for perm in itertools.permutations(range(5)))

puzzle.answer_a = max_thruster
print('Part1:', puzzle.answer_a)


puzzle.answer_b = max(try_perm_part2(program, perm) for perm in itertools.permutations(range(5, 10)))
print('Part2:', puzzle.answer_b)
