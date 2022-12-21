from operator import add, sub, floordiv, mul
import z3
from current_puzzle import current_puzzle

opers = {'+': add, '-': sub, '/': floordiv, '*': mul}


def do_monkey(monkey, part2=False):
    if part2:
        assert monkey != 'root'
        if monkey == 'humn':
            return monkey
    rule = monkeys[monkey]
    if rule.isnumeric():
        return int(rule)
    m1, op, m2 = rule.split()
    m1, m2 = do_monkey(m1, part2), do_monkey(m2, part2)
    if type(m1) == int and type(m2) == int:
        return opers[op](m1, m2)
    else:
        return f"({m1} {op} {m2})"


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

monkeys = dict()
for line in input_data.splitlines():
    # if 'humn' in line: print(line)
    s = line.split(': ')
    monkeys[s[0]] = s[1]

puzzle.answer_a = do_monkey('root')
print('Part1:', puzzle.answer_a)

m1, _, m2 = monkeys['root'].split()
m1, m2 = str(do_monkey(m1, part2=True)), str(do_monkey(m2, part2=True))
s = z3.Solver()
humn = z3.Int('humn')
s.add(eval(m1) == eval(m2))
assert s.check() == z3.sat

puzzle.answer_b = s.model().eval(humn)
print('Part2:', puzzle.answer_b)
