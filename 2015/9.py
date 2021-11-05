from current_puzzle import current_puzzle
from collections import defaultdict
import re


def dfs(node, path, dist):
    global min_dist, max_dist
    path.append(node)
    if len(path) == len(dists):
        min_dist = min(min_dist, dist)
        max_dist = max(max_dist, dist)
    else:
        for dest in dists[node]:
            if dest not in path:
                dfs(dest, path, dist + dists[node][dest])
    path.pop()


pat = re.compile(r'(\S+) to (\S+) = (\d+)')
puzzle = current_puzzle()
input_data = puzzle.input_data

dists = defaultdict(dict)
for line in input_data.splitlines():
    src, dest, dist = pat.match(line).groups()
    dists[src][dest] = dists[dest][src] = int(dist)

min_dist = float('inf')
max_dist = 0
for src in dists:
    dfs(src, [], 0)

puzzle.answer_a = min_dist
print('Part1:', puzzle.answer_a)
puzzle.answer_b = max_dist
print('Part2:', puzzle.answer_b)
