from collections import defaultdict

from current_puzzle import current_puzzle


class Graph:
    def __init__(self):
        self.adj = defaultdict(set)
        self.lengths = dict()

    def add_edge(self, a, b):
        self.adj[a].add(b)
        self.adj[b].add(a)

    def dfs(self, start=0):
        self.lengths = dict()
        stack = [(start, 0)]
        while stack:
            pos, depth = stack.pop()
            if pos in self.lengths:
                continue
            self.lengths[pos] = depth
            for to in self.adj[pos]:
                stack.append((to, depth + 1))


puzzle = current_puzzle()
directions = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
g = Graph()
pos = {0}
starts = ends = None
stack = []
for c in puzzle.input_data:
    if c in 'NESW':
        direction = directions[c]
        for p in pos:
            g.add_edge(p, p+direction)
        pos = {p + direction for p in pos}
    elif c == '(':
        stack.append((starts, ends))      # groups can be nested
        starts, ends = set(pos), set()
    elif c == '|':
        ends.update(pos)
        pos = set(starts)
    elif c == ')':
        pos.update(ends)
        starts, ends = stack.pop()

g.dfs()
puzzle.answer_a = max(g.lengths.values())
print('Part1:', puzzle.answer_a)
puzzle.answer_b = sum(1 for node in g.lengths if g.lengths[node] >= 1000)
print('Part2:', puzzle.answer_b)
