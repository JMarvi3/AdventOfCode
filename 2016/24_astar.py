from aocd.models import Puzzle
from collections import deque, defaultdict
import heapq
import time

start = time.perf_counter()


maze = dict()
points = dict()
for y, line in enumerate(Puzzle(2016, 24).input_data.splitlines()):
    for x, c in enumerate(line):
        if c == '#':
            continue
        maze[(x, y)] = c
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


def astar(points, maze, adj):
    count = 0
    visited = set()
    q = [()]
    q = [(len(points) - 1, 0, '0', '')]
    heapq.heapify(q)
    while q:
        score, dist, pt, path = heapq.heappop(q)
        path += pt
        if len(path) == len(points):
            print(count)
            return dist, path
        for j in (point for point in points if point not in path):
            if path + j not in visited:
                if pt not in adj or j not in adj[pt]:
                    count += 1
                    adj[pt][j] = adj[pt][j] = bfs(points[pt], points[j], maze)
                new_dist = dist + adj[pt][j]
                new_path = path + j
                t = (len(points) - len(new_path), new_dist, j, path)
                in_q = False
                for i in range(len(q)):
                    if q[i][1] == j:
                        in_q = True
                        if t < q[i]:
                            q[i] = t
                            heapq.heapify(q)
                        break
                if not in_q:
                    heapq.heappush(q, t)
        visited.add(path)
    return -1


adj = defaultdict(lambda: defaultdict(int))
print(astar(points, maze, adj))

print(1000*(time.perf_counter()-start))
