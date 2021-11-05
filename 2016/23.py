from aocd.models import Puzzle


def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


def run(regs, insts):
    def decode(y):
        if y in 'abcd':
            return regs[y]
        else:
            return int(y)

    pc = 0
    while 0 <= pc < len(insts):
        inst = insts[pc]
        if inst[0] == 'cpy':
            if inst[2] in 'abcd':
                regs[inst[2]] = decode(inst[1])
        elif inst[0] == 'inc':
            if inst[1] in 'abcd':
                regs[inst[1]] += 1
        elif inst[0] == 'dec':
            if inst[1] in 'abcd':
                regs[inst[1]] -= 1
        elif inst[0] == 'jnz':
            if decode(inst[1]) != 0:
                pc += decode(inst[2]) - 1
        elif inst[0] == 'tgl':
            dest = pc + decode(inst[1])
            if 0 <= dest < len(insts):
                if len(insts[dest]) == 2:
                    insts[dest][0] = 'dec' if insts[dest][0] == 'inc' else 'inc'
                elif len(insts[dest]) == 3:
                    insts[dest][0] = 'cpy' if insts[dest][0] == 'jnz' else 'jnz'
        pc += 1
    return regs


insts = [line.split() for line in Puzzle(2016, 23).input_data.splitlines()]
add = int(insts[19][1]) * int(insts[20][1])
regs = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
print('part1:', run(regs, insts)['a'], fact(7) + add)
print('part2:', fact(12) + add)
