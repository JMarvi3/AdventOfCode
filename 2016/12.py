from aocd.models import Puzzle


def run(regs):
    def decode(y):
        if y in 'abcd':
            return regs[y]
        else:
            return int(y)

    pc = 0
    while 0 <= pc < len(insts):
        inst = insts[pc]
        if inst[0] == 'cpy':
            regs[inst[2]] = decode(inst[1])
        elif inst[0] == 'inc':
            regs[inst[1]] += 1
        elif inst[0] == 'dec':
            regs[inst[1]] -= 1
        elif inst[0] == 'jnz':
            if decode(inst[1]) != 0:
                pc += decode(inst[2]) - 1
        pc += 1
    return regs


insts = [line.split() for line in Puzzle(2016, 12).input_data.splitlines()]

print('part1:', run({'a': 0, 'b': 0, 'c': 0, 'd': 0})['a'])
print('part2:', run({'a': 0, 'b': 0, 'c': 1, 'd': 0})['a'])
