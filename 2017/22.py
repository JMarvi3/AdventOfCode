from aocd.models import Puzzle
input_data = "..#\n#..\n..."
input_data = Puzzle(2017, 22).input_data

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
cur_dir = 0
field = dict()
y = x = 0
for line in input_data.splitlines():
    x = 0
    for c in line:
        if c == '#':
            field[(x, y)] = c
        x += 1
    y += 1


cur_pos = (x//2, y//2)
part2_saved = field.copy(), cur_dir, tuple(cur_pos)

infections = 0
for _ in range(10_000):
    if cur_pos in field:
        cur_dir = (cur_dir + 1) % 4
        del field[cur_pos]
    else:
        cur_dir = (cur_dir - 1) % 4
        infections += 1
        field[cur_pos] = '#'
    cur_pos = (cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1])
print('Part1:', infections)

cur_pos = (x//2, y//2)

infections = 0
field, cur_dir, cur_pos = part2_saved
for _ in range(10000000):
    status = field.get(cur_pos, None)
    if status is None:
        cur_dir = (cur_dir - 1) % 4
        field[cur_pos] = 'W'
    elif status == 'W':
        field[cur_pos] = '#'
        infections += 1
    elif status == '#':
        cur_dir = (cur_dir + 1) % 4
        field[cur_pos] = 'F'
    elif status == 'F':
        del field[cur_pos]
        cur_dir = (cur_dir + 2) % 4
    cur_pos = (cur_pos[0] + dirs[cur_dir][0], cur_pos[1] + dirs[cur_dir][1])
print('Part2:', infections)
