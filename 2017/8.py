from aocd.models import Puzzle
from collections import defaultdict
from operator import gt, ge, lt, le, eq, ne, pos, neg

registers = defaultdict(int)
max_reg = 0

ops = {'>': gt, '>=': ge, '<': lt, '<=': le, '==': eq, '!=': ne, 'inc': pos, 'dec': neg}
for line in Puzzle(2017, 8).input_data.splitlines():
    dest, op, diff, _, src, comp, num = line.split()
    if ops[comp](registers[src], int(num)):
        registers[dest] += ops[op](int(diff))
        max_reg = max(max_reg, max(registers.values()))

print('Part1:', max(registers.values()))
print('Part2:', max_reg)
