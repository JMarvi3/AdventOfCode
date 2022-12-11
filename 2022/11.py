from copy import deepcopy
from operator import mul, add
from current_puzzle import current_puzzle
import aoc_lib


class Monkey:
    monkeys = dict()
    common_multiple = 1

    def __init__(self, text):
        text = text.splitlines()
        self.number = aoc_lib.findall('{:d}', text[0])[0]
        self.items = aoc_lib.findall('{:d}', text[1])
        op = text[2].split()
        self.operator = mul if op[-2] == '*' else add
        self.operand = op[-1] if op[-1] == 'old' else int(op[-1])
        self.test = aoc_lib.findall('{:d}', text[3])[0]
        self.true = aoc_lib.findall('{:d}', text[4])[0]
        self.false = aoc_lib.findall('{:d}', text[5])[0]
        self.count = 0
        Monkey.monkeys[self.number] = self
        Monkey.common_multiple *= self.test

    def do_stuff(self, part2=False):
        for item in self.items:
            self.count += 1
            item = self.operator(item, item if self.operand == 'old' else self.operand)
            if not part2:
                item //= 3
            item %= Monkey.common_multiple
            destination = self.true if item % self.test == 0 else self.false
            Monkey.monkeys[destination].items.append(item)
        self.items = []


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('11.example').read()

monkeys = [Monkey(chunk) for chunk in input_data.split('\n\n')]
part2_monkeys = deepcopy(monkeys)

for i in range(20):
    for monkey in monkeys:
        monkey.do_stuff()

counts = sorted(monkey.count for monkey in monkeys)
puzzle.answer_a = counts[-2] * counts[-1]
print('Part1:', puzzle.answer_a)

Monkey.monkeys = {monkey.number: monkey for monkey in part2_monkeys}

for i in range(10000):
    for monkey in part2_monkeys:
        monkey.do_stuff(part2=True)

counts = sorted(monkey.count for monkey in part2_monkeys)
puzzle.answer_b = counts[-2] * counts[-1]
print('Part2:', puzzle.answer_b)
