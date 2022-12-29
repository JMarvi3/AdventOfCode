from current_puzzle import current_puzzle
import re


def parse_moves(moves): return re.findall(r"([RL]|\d+)", moves)


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
board, moves = input_data.split('\n\n')
board = board.splitlines()
moves = parse_moves(moves)

maps = dict()
# This only works for my input
for x in range(0, 50):
    maps.update({(x, 99): (x, 199), (x, 200): (x, 100)})
for x in range(50, 100):
    maps.update({(x, -1): (x, 149), (x, 150): (x, 0)})
for x in range(100, 150):
    maps.update({(x, -1): (x, 49), (x, 50): (x, 0)})

for y in range(0, 50):
    maps.update({(49, y): (149, y), (150, y): (50, y)})
for y in range(50, 100):
    maps.update({(49, y): (99, y), (100, y): (50, y)})
for y in range(100, 150):
    maps.update({(-1, y): (99, y), (100, y): (0, y)})
for y in range(150, 200):
    maps.update({(-1, y): (49, y), (50, y): (0, y)})

x, y = 50, 0
curr_dir = 0
for move in moves:
    if move == 'L':
        curr_dir = (curr_dir - 1) % len(dirs)
    elif move == 'R':
        curr_dir = (curr_dir + 1) % len(dirs)
    else:
        d = dirs[curr_dir]
        for i in range(int(move)):
            new_pt = x + d[0], y + d[1]
            if new_pt in maps:
                new_pt = maps[new_pt]
            if board[new_pt[1]][new_pt[0]] == '#':
                break
            x, y = new_pt


puzzle.answer_a = 1000 * (y+1) + 4 * (x+1) + curr_dir
print('Part1:', puzzle.answer_a)


maps = dict()
# This only works for my input
for x in range(0, 50):
    maps.update({(x, 99, 3): (50, x+50, 0), (x, 200, 1): (x+100, 0, 1)})
for x in range(50, 100):
    maps.update({(x, -1, 3): (0, x+100, 0), (x, 150, 1): (49, x+100, 2)})
for x in range(100, 150):
    maps.update({(x, -1, 3): (x-100, 199, 3), (x, 50, 1): (99, x-50, 2)})

for y in range(0, 50):
    maps.update({(49, y, 2): (0, 149-y, 0), (150, y, 0): (99, 149-y, 2)})
for y in range(50, 100):
    maps.update({(49, y, 2): (y-50, 100, 1), (100, y, 0): (y+50, 49, 3)})
for y in range(100, 150):
    maps.update({(-1, y, 2): (50, 149-y, 0), (100, y, 0): (149, 149-y, 2)})
for y in range(150, 200):
    maps.update({(-1, y, 2): (y-100, 0, 1), (50, y, 0): (y-100, 149, 3)})

x, y = 50, 0
curr_dir = 0
for move in moves:
    if move == 'L':
        curr_dir = (curr_dir - 1) % len(dirs)
    elif move == 'R':
        curr_dir = (curr_dir + 1) % len(dirs)
    else:
        d = dirs[curr_dir]
        for i in range(int(move)):
            new_x, new_y, new_dir = x + d[0], y + d[1], curr_dir
            if (new_x, new_y, new_dir) in maps:
                new_x, new_y, new_dir = maps[(new_x, new_y, new_dir)]
            if board[new_y][new_x] == '#':
                break
            if new_dir != curr_dir:
                d = dirs[new_dir]
            x, y, curr_dir = new_x, new_y, new_dir

puzzle.answer_b = 1000 * (y+1) + 4 * (x+1) + curr_dir
print('Part2:', puzzle.answer_b)
