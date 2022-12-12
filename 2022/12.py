from collections import deque
from current_puzzle import current_puzzle
import aoc_lib
from time import perf_counter

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

# # Faster and cleaner
# import networkx
#
# grid = input_data.splitlines()
# COLS, ROWS = range(len(grid[0])), range(len(grid))
# height = {k: ord(v) for k, v in zip('SEabcdefghijklmnopqrstuvwxyz', 'azabcdefghijklmnopqrstuvwxyz')}
# g = networkx.DiGraph()
# for x in COLS:
#     for y in ROWS:
#         if grid[y][x] == 'S':
#             start = (x, y)
#         elif grid[y][x] == 'E':
#             end = (x, y)
#         for new_x, new_y in (aoc_lib.add_pts((x, y), d) for d in aoc_lib.dirs):
#             if new_x in COLS and new_y in ROWS:
#                 g.add_edge((x, y), (new_x, new_y), climb=height[grid[new_y][new_x]] - height[grid[y][x]])
# g.remove_edges_from([edge for edge in g.edges(data=True) if edge[2]['climb'] > 1])
# paths = networkx.shortest_path_length(g, target=end)
# print(f"Part1: {paths[start]}")
# print(f"Part2: {min(v for (x, y), v in paths.items() if grid[y][x] == 'a')}")
