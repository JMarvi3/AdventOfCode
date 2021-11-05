from aocd.models import Puzzle
from hex_lib import Hex, hex_neighbor, hex_length

dirs = ['n', 'ne', 'se', 's', 'sw', 'nw']
pos = Hex(0, 0, 0)
path = Puzzle(2017, 11).input_data.split(',')
max_dist = 0
for step in path:
    pos = hex_neighbor(pos, dirs.index(step))
    dist = hex_length(pos)
    max_dist = max(max_dist, dist)

print('Part1:', dist)
print('Part2:', max_dist)


# dirs = {'n': (1, -1, 0), 'ne': (1, 0, -1), 'se': (0, 1, -1), 's': (-1, 1, 0), 'sw': (-1, 0, 1), 'nw': (0, -1, 1)}
#
# pos = [0, 0, 0]
# path = Puzzle(2017, 11).input_data.split(',')
# max_dist = 0
# for step in path:
#     for time in range(3):
#         pos[time] += dirs[step][time]
#     dist = max(map(abs, pos))
#     max_dist = max(max_dist, dist)
#
# print('Part1:', dist)
# print('Part2:', max_dist)
