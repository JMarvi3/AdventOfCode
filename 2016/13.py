from aocd.models import Puzzle
from collections import defaultdict, deque


def bin_digits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def gen(x, y, fav):
    global maze
    if x not in maze or y not in maze[x]:
        maze[x][y] = '.' if bin_digits(x * x + 3 * x + 2 * x * y + y + y * y + fav) % 2 == 0 else '#'
    return maze[x][y]


def bfs(src, dest, fav, max_dist=None):
    min_dist = float('inf')
    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    visited = set()
    q = deque()
    q.appendleft((src, 0))
    while q:
        p, d = q.pop()
        if p == dest:
            if max_dist and d <= max_dist:
                return True
            min_dist = min(min_dist, d)
        for move in moves:
            x, y = p[0] + move[0], p[1] + move[1]
            if x >= 0 and y >= 0 and (x, y) not in visited and gen(x, y, fav) == '.':
                visited.add((x, y))
                q.appendleft(((x, y), d + 1))
    if max_dist:
        return min_dist <= max_dist
    return min_dist


fav = int(Puzzle(2016, 13).input_data)
maze = defaultdict(lambda: defaultdict(str))
part1 = bfs((1, 1), (31, 39), fav)
print('part1:', part1)
part2 = sum(bfs((1, 1), (i, j), fav, 50) for i in range(part1 + 1) for j in range(part1 + 1))
print('part2:', part2)
