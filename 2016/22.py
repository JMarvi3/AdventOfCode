from current_puzzle import current_puzzle
from collections import defaultdict
import re

# http://codepen.io/anon/pen/BQEZzK/

puzzle = current_puzzle()

SIZE, USED, AVAIL = 0, 1, 2

num_pat = re.compile(r'\d+')
nodes = defaultdict(list)
max_x = max_y = 0
for line in puzzle.input_data.splitlines()[2:]:
    nums = list(map(int, num_pat.findall(line)))
    nodes[(nums[0], nums[1])] = nums[2:5]
    max_x = max(max_x, nums[0])
    max_y = max(max_y, nums[1])

viable = 0
for a in nodes:
    for b in nodes:
        if a != b and nodes[a][USED] != 0 and nodes[a][USED] <= nodes[b][AVAIL]:
            viable += 1

puzzle.answer_a = viable
print('Part1:', puzzle.answer_a)

empty = next(node for node in nodes if nodes[node][USED] == 0)
min_size = min(node[SIZE] for node in nodes.values())
# for y in range(max_y+1):
#     for x in range(max_x+1):
#         node = nodes[(x, y)]
#         if node[USED] == 0:
#             s = ' __'
#         elif node[USED] > min_size:
#             s = ' ##'
#         else:
#             s = str(node[USED]).rjust(3)
#         print(s, end='')
#     print()

# This works for my two inputs.. the wall extends above and to the left and right of the empty node
first_wall = next((x, y) for x in range(max_x+1) for y in range(max_y+1) if nodes[(x, y)][USED] > min_size)
# assertion makes sure it holds true for this input
assert first_wall[0] <= empty[0] and first_wall[1] < empty[1] and \
       all(nodes[(x, first_wall[1])][USED] > min_size for x in range(first_wall[0], max_x+1))
puzzle.answer_b = (empty[0] - first_wall[0] + 1) * 2 + (max_x - empty[0]) + empty[1] + 5 * (max_x - 1)
print('Part2:', puzzle.answer_b)
