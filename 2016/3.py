from aocd.models import Puzzle

tris = []
possible = 0
for line in Puzzle(2016, 3).input_data.splitlines():
    tri = [int(i) for i in line.split()]
    tris.append(tri)
    if sum(tri) - 2*max(tri) > 0:
        possible += 1

print('part1:', possible)

possible = 0
last_tri = None
for j in range(3):
    for i in range(0, len(tris), 3):
        tri = [tris[i][j], tris[i+1][j], tris[i+2][j]]
        if sum(tri) - 2 * max(tri) > 0:
            possible += 1

print('part2:', possible)

