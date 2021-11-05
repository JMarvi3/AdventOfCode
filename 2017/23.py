from collections import defaultdict
from aocd.models import Puzzle


def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


program = [line.split() for line in Puzzle(2017, 23).input_data.splitlines()]
regs = defaultdict(int)
pc = 0
mul_count = 0
while 0 <= pc < len(program):
    inst = program[pc]
    if inst[2].isalpha():
        op = regs[inst[2]]
    else:
        op = int(inst[2])
    if inst[0] == 'set':
        regs[inst[1]] = op
    elif inst[0] == 'sub':
        regs[inst[1]] -= op
    elif inst[0] == 'mul':
        mul_count += 1
        regs[inst[1]] *= op
    elif inst[0] == 'jnz':
        if (regs[inst[1]] if inst[1].isalpha() else int(inst[1])) != 0:
            pc += op - 1
    pc += 1
print('Part1:', mul_count)

h = 0
b = 67

mul_count = (b-2)**2    # The fast way
b = b * 100 + 100_000
c = b + 17_000
while True:
    h += not is_prime(b)
    if b == c:
        break
    b += 17
print('Part2:', h)
