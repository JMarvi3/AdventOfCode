from collections import deque
from current_puzzle import current_puzzle
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('12.example').read()

grid = dict()
start = goal = None
for y, row in enumerate(input_data.splitlines()):
    for x, col in enumerate(row):
        if col == 'S':
            start = (x, y)
            grid[start] = 'a'
        elif col == 'E':
            goal = (x, y)
            grid[goal] = 'z'
        else:
            grid[(x, y)] = col


def dfs(start, goal):
    visited = set()
    q = deque([(start, 1)])
    while q:
        pt, path = q.popleft()
        if pt in visited:
            continue
        if pt == goal:
            return path - 1
        visited.add(pt)
        for d in aoc_lib.dirs:
            new_pt = aoc_lib.add_pts(pt, d)
            if new_pt in grid and new_pt not in visited and ord(grid[new_pt]) - ord(grid[pt]) <= 1:
                q.append((new_pt, path + 1))
    return float('inf')


min_path = dfs(start, goal)
# print(min_path)
puzzle.answer_a = min_path
print('Part1:', puzzle.answer_a)

min_path = min(dfs(pt, goal) for pt in grid if grid[pt] == 'a')
# print(min_path)
puzzle.answer_b = min_path
print('Part2:', puzzle.answer_b)
