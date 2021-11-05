from aocd.models import Puzzle
from collections import deque
from itertools import permutations
import time
start = time.perf_counter()

maze = set()
points = dict()
for y, line in enumerate(Puzzle(2016, 24).input_data.splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            continue
        maze.add((x, y))
        if c in '0123456789':
            points[c] = (x, y)


def bfs(src, dest, maze):
    visited = set()
    q = deque([(src, 0)])
    while q:
        pt, dist = q.pop()
        if pt == dest:
            return dist
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pt = (pt[0] + dir[0], pt[1] + dir[1])
            if new_pt in maze and new_pt not in visited:
                visited.add(new_pt)
                q.appendleft((new_pt, dist + 1))
    return -1


adj = dict()
for i in points:
    for j in points:
        if i == j or (j, i) in adj:
            continue
        dist = bfs(points[i], points[j], maze)
        assert dist > 0
        adj[(i, j)] = adj[(j, i)] = dist


min_dist = float('inf')
min_dist_return = float('inf')
point_str = ''.join(point for point in points if point != '0')
for perm in permutations(point_str):
    prev = '0'
    dist = adj[('0', perm[0])] + sum(adj[(perm[i], perm[i + 1])] for i in range(len(point_str) - 1))
    min_dist = min(min_dist, dist)
    min_dist_return = min(min_dist_return, dist + adj[(perm[-1], '0')])

print('part1:', min_dist)
print('part2:', min_dist_return)

print(1000*(time.perf_counter() - start))
