from collections import defaultdict, deque
from current_puzzle import current_puzzle
from random import shuffle
import re
import time

start = time.perf_counter()

puzzle = current_puzzle()
input_data = puzzle.input_data

replacements = defaultdict(list)
reverse = dict()
for line in input_data.splitlines():
    if '=>' in line:
        f, t = line.split(' => ')
        replacements[f].append(t)
        reverse[t] = f
    elif len(line) != 0:
        molecule = line

combs = set()
elems = re.findall(r'([A-Z][a-z]*)', molecule)
for i, elem in enumerate(elems):
    c = elems.copy()
    for r in replacements[elem]:
        c[i] = r
        combs.add(''.join(c))

puzzle.answer_a = len(combs)
print('Part1:', puzzle.answer_a)

part1 = time.perf_counter()

min_count = float('inf')
froms = list(reverse.keys())
for i in range(10_000):
    s = str(molecule)
    count = 0
    while s != 'e':
        replaced = False
        for f in froms:
            if f in s:
                count += s.count(f)
                s = s.replace(f, reverse[f])
                replaced = True
        if not replaced:
            shuffle(froms)
            count = 0
            s = str(molecule)
    if count < min_count:
        min_count = count
    shuffle(froms)

puzzle.answer_b = min_count
print('Part2:', puzzle.answer_b)

end = time.perf_counter()
print(f"time: {end-start:.3f}s total, {part1-start:.3f}s / {end-part1:.3f}s")
