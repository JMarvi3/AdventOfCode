from current_puzzle import current_puzzle
import aoc_lib
import more_itertools
from functools import reduce


def priority(s):
    assert len(s) == 1
    item = s.pop()
    if item > 'Z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
elves = input_data.split('\n')


# total = sum(priority(reduce(set.intersection, map(set, more_itertools.divide(2, elf)))) for elf in elves)
# part2_total = sum(priority(reduce(set.intersection, map(set, group))) for group in more_itertools.chunked(elves, 3))

total = 0
for elf in elves:
    half_len = len(elf)//2
    common = set(elf[:half_len]).intersection(elf[half_len:])
    total += priority(common)

part2_total = 0
for i in range(0, len(elves), 3):
    common = set(elves[i]).intersection(elves[i + 1], elves[i + 2])
    part2_total += priority(common)

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

puzzle.answer_b = part2_total
print('Part2:', puzzle.answer_b)
