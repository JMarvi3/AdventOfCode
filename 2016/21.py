from aocd.models import Puzzle
import re
from itertools import permutations

num_pat = re.compile(r'\d+')

rules = Puzzle(2016, 21).input_data.splitlines()


def scramble(s, rules):
    s = list(s)
    for rule in rules:
        if rule[:6] == 'swap p':
            x, y = list(map(int, num_pat.findall(rule)))
            s[x], s[y] = s[y], s[x]
        elif rule[:6] == 'swap l':
            x, y = s.index(rule[12]), s.index(rule[26])
            s[x], s[y] = s[y], s[x]
        elif rule[:6] == 'rotate':
            if rule[7] == 'l':
                x = next(map(int, num_pat.findall(rule)))
                s = s[x:] + s[:x]
            elif rule[7] == 'r':
                x = next(map(int, num_pat.findall(rule)))
                s = s[-x:] + s[:-x]
            elif rule[7] == 'b':
                x = s.index(rule[-1])
                if x >= 4:
                    x += 1
                x = (x + 1) % len(s)
                s = s[-x:] + s[:-x]
        elif rule[:7] == 'reverse':
            x, y = list(map(int, num_pat.findall(rule)))
            s = s[:x] + s[x:y + 1][::-1] + s[y + 1:]
        elif rule[:4] == 'move':
            x, y = list(map(int, num_pat.findall(rule)))
            if y > x:
                s = s[0:x] + s[x + 1:y + 1] + [s[x]] + s[y + 1:]
            elif y < x:
                s = s[0:y] + [s[x]] + s[y:x] + s[x + 1:]
        # print(rule, ''.join(s))
    return ''.join(s)


rules = Puzzle(2016, 21).input_data.splitlines()
print('part1:', scramble('abcdefgh', rules))


for perm in permutations('abcdefgh'):
    if scramble(perm, rules) == 'fbgdceah':
        print('part2:', ''.join(perm))
        break
