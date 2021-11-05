# from pprint import pprint
# import sys
from current_puzzle import current_puzzle


def run(registers):
    pc = 0
    while 0 <= pc < len(memory):
        op, args = memory[pc]
        # pprint((pc, op, args, registers), stream=sys.stdout)
        if op == 'hlf':
            registers[args[0]] //= 2
            pc += 1
        elif op == 'tpl':
            registers[args[0]] *= 3
            pc += 1
        elif op == 'inc':
            registers[args[0]] += 1
            pc += 1
        elif op == 'jmp':
            pc += int(args[0])
        elif op == 'jie':
            if registers[args[0][0]] % 2 == 0:
                pc += int(args[1])
            else:
                pc += 1
        elif op == 'jio':
            if registers[args[0][0]] == 1:
                pc += int(args[1])
            else:
                pc += 1
        # print(registers)
    return registers


puzzle = current_puzzle()
input_data = puzzle.input_data
memory = []
for line in input_data.splitlines():
    op, args = line.split(maxsplit=1)
    memory.append((op, args.split()))


puzzle.answer_a = run({'a': 0, 'b': 0})['b']
print('Part1:', puzzle.answer_a)
puzzle.answer_b = run({'a': 1, 'b': 0})['b']
print('Part2:', puzzle.answer_b)
