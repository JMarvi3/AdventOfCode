from aocd.models import Puzzle
from collections import defaultdict


def run(pc, regs, queue, part2=False):
    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return regs[x]

    sounds = []
    while pc < len(program):
        op = program[pc]
        if op[0] == 'snd':
            sounds.append(get_value(op[1]))
        elif op[0] == 'set':
            regs[op[1]] = get_value(op[2])
        elif op[0] == 'add':
            regs[op[1]] += get_value(op[2])
        elif op[0] == 'mul':
            regs[op[1]] *= get_value(op[2])
        elif op[0] == 'mod':
            regs[op[1]] %= get_value(op[2])
        elif op[0] == 'rcv':
            if not part2:
                if get_value(op[1]) != 0:
                    return sounds[-1]
            else:
                if queue:
                    regs[op[1]] = queue.pop(0)
                else:
                    return pc, regs, sounds
        elif op[0] == 'jgz':
            if get_value(op[1]) > 0:
                pc += get_value(op[2]) - 1
        pc += 1
    print('Error', pc)
    exit(-1)


program = [line.split() for line in Puzzle(2017, 18).input_data.strip().splitlines()]

print('Part1:', run(0, defaultdict(int), []))

data = [[0, defaultdict(int, {'p': pid}), []] for pid in range(2)]
count = 0
while True:
    count += len(data[0][2])
    for pid in range(2):
        data[pid][0], data[pid][1], data[1-pid][2] = run(*data[pid], True)
    if not data[0][2] and not data[1][2]:
        break
print('Part2:', count)
