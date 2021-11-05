from aocd.models import Puzzle
sample = "     | \n\
     |  +--+     \n\
     A  |  C     \n\
 F---|----E|--+  \n\
     |  |  |  D  \n\
     +B-+  +--+  "


dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
#field = sample.splitlines()
field = Puzzle(2017, 19).input_data.splitlines()

x, y = field[0].index('|'), 0
hits = ''
dire = 0
steps = 0
while 0 <= y <= len(field) and 0 <= x < len(field[y]) and field[y][x] != ' ':
    steps += 1
    if field[y][x].isalpha():
        hits += field[y][x]
    elif field[y][x] == '+':
        for diff in [-1, 1]:
            new_dir = (dire + diff) % 4
            new_x, new_y = x + dirs[new_dir][0], y + dirs[new_dir][1]
            if 0 <= new_y < len(field) and 0 <= new_x < len(field[new_y]) and field[new_y][new_x] != ' ':
                dire = new_dir
                break
    x += dirs[dire][0]
    y += dirs[dire][1]
print('Part1:', hits)
print('Part2:', steps)
