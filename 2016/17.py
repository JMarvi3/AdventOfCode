from aocd.models import Puzzle
from collections import deque
from hashlib import md5


def bfs(key, dest):
    max_dist = 0
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    q = deque()
    m = md5()
    m.update(bytes(key, 'utf-8'))
    q.appendleft(((0, 0), '', m))
    answer = None
    while q:
        p, path, m = q.pop()
        if p == dest:
            max_dist = max(len(path), max_dist)
            if not answer:
                answer = path
            continue
        keys = m.hexdigest()[:4]
        for i, move in enumerate('UDLR'):
            x, y = p[0] + moves[i][0], p[1] + moves[i][1]
            if 0 <= x < 4 and 0 <= y < 4 and keys[i] in 'bcdef':
                new_m = m.copy()
                new_m.update(bytes(move, 'utf-8'))
                q.appendleft(((x, y), path + move, new_m))

    print(key, answer, max_dist)


bfs('ihgpwlah', (3, 3))
bfs('kglvqrro', (3, 3))
bfs('ulqzkmiv', (3, 3))
bfs(Puzzle(2016, 17).input_data, (3, 3))
