import re
from copy import deepcopy

from current_puzzle import current_puzzle
import aoc_lib


class Monkey:
    def __init__(self, text):
        text = text.splitlines()
        self.number = aoc_lib.findall('{:d}', text[0])[0]
        self.items = aoc_lib.findall('{:d}', text[1])
        op = text[2].split()
        self.op = op[-2], op[-1]
        self.test = int(text[3].split()[-1])
        self.true = int(text[4].split()[-1])
        self.false = int(text[5].split()[-1])
        self.count = 0

    def do_stuff(self, monkeys: dict, worry_mitigation=None):
        # print(monkey.number)
        for item in self.items:
            # print('item', item)
            self.count += 1
            right = int(self.op[1]) if self.op[1] != 'old' else item
            if self.op[0] == '*':
                # print('multiplied by', right)
                item *= right
            else:
                # print('increased by', right)
                item += right
            if worry_mitigation is None:
                item //= 3
            else:
                item %= worry_mitigation
            if item % self.test == 0:
                # print('passed', item, 'to', self.true)
                monkeys[self.true].items.append(item)
            else:
                # print('passed', item, 'to', self.false)
                monkeys[self.false].items.append(item)
        self.items = []

    def __repr__(self):
        return f"{self.number}: ({self.count}) {self.items}"


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('11.example').read()

worry = False
monkeys = dict()
for monkey in input_data.split('\n\n'):
    node = Monkey(monkey)
    monkeys[node.number] = node

common = 1
for monkey in monkeys.values():
    common *= monkey.test

part2_monkeys = deepcopy(monkeys)

for i in range(20):
    for monkey in monkeys.values():
        monkey.do_stuff(monkeys)

counts = sorted(monkey.count for monkey in monkeys.values())
puzzle.answer_a = counts[-2] * counts[-1]
print('Part1:', puzzle.answer_a)

for i in range(10000):
    for monkey in part2_monkeys.values():
        monkey.do_stuff(part2_monkeys, common)

counts = sorted(monkey.count for monkey in part2_monkeys.values())
puzzle.answer_b = counts[-2] * counts[-1]
print('Part2:', puzzle.answer_b)
