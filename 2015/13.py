from collections import defaultdict
import re
from current_puzzle import current_puzzle


def dfs(person, arr: list, h):
    global max_h, best
    arr.append(person)
    if len(arr) == len(rules)+1 and arr[-1] == arr[0]:
        if h > max_h:
            best = list(arr)
            max_h = h
    else:
        for n in rules[person]:
            if n == arr[0] or n not in arr:
                dfs(n, arr, h + rules[person][n] + rules[n][person])
    arr.pop()


puzzle = current_puzzle()
input_data = puzzle.input_data

pat = re.compile(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).')

rules = defaultdict(dict)
people = []

for line in input_data.splitlines():
    f, gain, n, t = pat.match(line).groups()
    rules[f][t] = (1 if gain == 'gain' else -1) * int(n)
    people.append(f)

max_h = 0
best = []
dfs(people[0], [], 0)

puzzle.answer_a = max_h
print('Part1:', puzzle.answer_a, best)

worst = []
min_h = float('inf')
for i in range(len(best) - 1):
    h = rules[best[i]][best[i+1]] + rules[best[i+1]][best[i]]
    if h < min_h:
        worst = best[i:i+2]
        min_h = h

puzzle.answer_b = max_h - min_h
print('Part2:', puzzle.answer_b, f"seated between {worst[0]} and {worst[1]}.")
