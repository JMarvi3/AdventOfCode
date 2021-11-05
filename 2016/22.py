from aocd.models import Puzzle
from collections import defaultdict, deque

import re

SIZE, USED, AVAIL = 0, 1, 2

num_pat = re.compile(r'\d+')
nodes = defaultdict(list)
for line in Puzzle(2016, 22).input_data.splitlines()[2:]:
    nums = list(map(int, num_pat.findall(line)))
    nodes[(nums[0], nums[1])] = nums[2:]

viable = 0
for a in nodes:
    for b in nodes:
        if a != b and nodes[a][USED] != 0 and nodes[a][USED] <= nodes[b][AVAIL]:
            viable += 1
print(viable)

max_x = max(node[0] for node in nodes if node[1] == 0)
print(max_x)


def bfs(src, dest, init_nodes):
    q = deque()
    q.appendleft((src, 0, init_nodes, [src]))
    visited = set([src])
    while q:
        pt, dist, nodes, path = q.pop()
        if pt == dest:
            return dist, nodes, path
        for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_pt = (pt[0] + dir[0], pt[1] + dir[1])
            if new_pt in nodes and new_pt not in visited and nodes[pt][AVAIL] >= nodes[new_pt][USED]:
                new_nodes = nodes.copy()
                new_nodes[pt] = list(nodes[pt])
                new_nodes[new_pt] = list(nodes[new_pt])
                new_nodes[pt][AVAIL] -= nodes[new_pt][USED]
                new_nodes[pt][USED] += nodes[new_pt][USED]
                new_nodes[new_pt][AVAIL] += nodes[new_pt][USED]
                new_nodes[new_pt][USED] = 0
                visited.add(new_pt)
                q.appendleft((new_pt, dist + 1, new_nodes, path + [new_pt]))
        return -1, init_nodes, []


min_dist = float('inf')
min_sol = ((0, 0), nodes, [])
for pt in nodes:
    if pt != (0, 0):
        dist, new_nodes, path = bfs(pt, (0, 0), nodes)
        print(pt, dist, path)
        if 0 <= dist < min_dist:
            min_dist = dist
            min_sol = (pt, new_nodes, path)

print(min_dist, min_sol[0], min_sol[1])
