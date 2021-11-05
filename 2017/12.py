from aocd.models import Puzzle
from collections import deque


def dfs(start, adj):
    q = deque([start])
    visited = set()
    while q:
        program = q.pop()
        visited.add(program)
        for child in adj[program]:
            if child not in visited:
                q.appendleft(child)
    return visited


adj = dict()
for line in Puzzle(2017, 12).input_data.splitlines():
    program, neighbors = line.strip().split(' <-> ')
    adj[program] = neighbors.split(', ')

print('Part1:', len(dfs('0', adj)))

programs = set(adj.keys())
groups = 0
while programs:
    groups += 1
    programs -= dfs(programs.pop(), adj)

print('Part2:', groups)
