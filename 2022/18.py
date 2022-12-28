from collections import deque
from current_puzzle import current_puzzle


def find_outside_sa(pt):
    outside_sa = 0
    seen = set([pt])
    q = deque([pt])
    while q:
        pt = q.popleft()
        for d in dirs:
            new_pt = (pt[0] + d[0], pt[1] + d[1], pt[2] + d[2])
            if all(all_min-1 <= new_pt[i] <= all_max+1 for i in range(3)) and new_pt not in seen:
                if new_pt not in cubes:
                    seen.add(new_pt)
                    q.append(new_pt)
                else:
                    outside_sa += 1
    return outside_sa


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('18.example').read()

dirs = [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]

cubes = set()
for line in input_data.splitlines():
    cubes.add(tuple(map(int, line.split(','))))

sa = 0
all_min, all_max = float('inf'), -float('inf')

for cube in cubes:
    all_min = min(all_min, *cube)
    all_max = max(all_max, *cube)
    for d in dirs:
        if (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2]) not in cubes:
            sa += 1

puzzle.answer_a = sa
print('Part1:', puzzle.answer_a)

outside_sa = find_outside_sa((all_min-1, all_min-1, all_min-1))
puzzle.answer_b = outside_sa
print('Part2:', puzzle.answer_b)
