from current_puzzle import current_puzzle
import aoc_lib
import functools


def descend(obj):
    if obj in counts:
        return counts[obj]
    if orbits[obj] in counts:
        counts[obj] = counts[orbits[obj]] + 1
    else:
        counts[obj] = descend(orbits[obj]) + 1
    inners[obj] = (*inners[orbits[obj]], obj)
    return counts[obj]


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

orbits = {outer: inner for inner,outer in map(functools.partial(str.split, sep=')'), input_data.splitlines())}
inners = {'COM': ('COM',)}
counts = {'COM': 0}

total = sum(descend(outer) for outer in orbits)
puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

you, san = inners['YOU'], inners['SAN']
i = 0
while you[i] == san[i]:
    i += 1

puzzle.answer_b = len(you) + len(san) - 2 * i - 2
print('Part2:', puzzle.answer_b)
