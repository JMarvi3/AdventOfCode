from aocd.models import Puzzle


def run(a, insts):
    def decode(y):
        if y in 'abcd':
            return regs[y]
        else:
            return int(y)

    regs = {'a': a, 'b': 0, 'c': 0, 'd': 0}
    output = ''
    visited = set()
    pc = 0
    while 0 <= pc < len(insts):
        inst = insts[pc]
        if inst[0] == 'out':
            t = (pc, tuple(regs[c] for c in 'abcd'))
            if t in visited:
                return len(output) >= 2 and output[0] == '0' and output[-1] == '1'
            src = str(decode(inst[1]))
            if src not in '01':
                return False
            output += src
            if output[-2:] in ['00', '11']:
                return False
            visited.add(t)
        elif inst[0] == 'cpy':
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
                new_inst = list(insts[dest])
                if len(new_inst) == 2:
                    new_inst[0] = 'dec' if new_inst[0] == 'inc' else 'inc'
                elif len(new_inst) == 3:
                    new_inst[0] = 'cpy' if new_inst[0] == 'jnz' else 'jnz'
                insts[dest] = new_inst
        pc += 1
    return regs


insts = list(list(line.split()) for line in Puzzle(2016, 25).input_data.splitlines())
a = 0
while not run(a, insts):
    a += 1
print('part1:', a)
