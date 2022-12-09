import operator
import functools
from current_puzzle import current_puzzle
import networkx

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

dirs = [-1, 1j, +1, -1j]
heights = dict()
for y, row in enumerate(input_data.splitlines()):
    for x, c in enumerate(row):
        heights[x + y * 1j] = int(c)

g = networkx.Graph()
total = 0
for point in heights:
    height = heights[point]
    neighbor_pts = [point + dir for dir in dirs if (point+dir) in heights]
    min_neighbor = min(heights[pt] for pt in neighbor_pts)
    if height < min_neighbor:
        total += 1 + height
    elif height < 9:
        g.add_edges_from([(point, pt) for pt in neighbor_pts if heights[pt] < height])

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

sizes = sorted(map(len, networkx.connected_components(g)))

puzzle.answer_b = functools.reduce(operator.mul, sizes[-3:])
print('Part2:', puzzle.answer_b)

from operator import mul
from functools import reduce
from networkx import Graph, connected_components

heights = {x+y*1j: int(c) for y, row in enumerate(input_data.splitlines()) for x, c in enumerate(row) if c != '9'}
part2, part1 = zip(*sorted((len(comp), min(heights[pt] for pt in comp)) for comp in connected_components(Graph((pt, (pt+d)) for d in {-1j, 1, 1j, -1} for pt in heights if pt+d in heights))))
print(sum(part1)+len(part1), reduce(mul, part2[-3:]))

