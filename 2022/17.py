from current_puzzle import current_puzzle
import aoc_lib


def can_move_down(x, y, shape, board):
    return not any((x+dx, y+dy-1) in board for (dx, dy) in shape)


def can_move_left(x, y, shape, board):
    return not any((x+dx-1) < 0 or (x + dx - 1, y + dy) in board for (dx, dy) in shape)


def can_move_right(x, y, shape, board):
    return not any((x+dx+1) > 6 or (x + dx + 1, y + dy) in board for (dx, dy) in shape)


def draw_board():
    print('|' + '-'*7 + '|')
    for y in range(curr_top, -1, -1):
        print('|' + ''.join(board.get((x,y), '.') for x in range(7)) + '|')
    print()


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('17.example').read()

moves = input_data
shapes = []
for shape in ['####', '.#.\n###\n.#.', '..#\n..#\n###', '#\n#\n#\n#', '##\n##']:
    d = dict()
    for y, row in enumerate(reversed(shape.splitlines())):
        for x, c in enumerate(row):
            if c == '#':
                d[(x, y)] = '#'
    shapes.append((d, y))


move_idx = 0
curr_top = 0
board = {(x, 0): '-' for x in range(7)}
seen = dict()
top = dict()

BIG_NUM = 10**12
for i in range(BIG_NUM):
    shape, height = shapes[i % len(shapes)]
    x, y = 2, curr_top + 4
    while True:
        move = moves[move_idx % len(moves)]
        move_idx += 1
        if move == '<':
            if can_move_left(x, y, shape, board):
                x -= 1
        elif move == '>':
            if can_move_right(x, y, shape, board):
                x += 1
        if can_move_down(x, y, shape, board):
            y -= 1
        else:
            # All the way settled
            break
    board.update({(x+dx, y+dy): '#' for (dx, dy) in shape})

    curr_top = max(curr_top, y+height)
    top[i + 1] = curr_top
    key = (frozenset((x, curr_top - y) for (x, y) in board if curr_top - 50 <= y <= curr_top), i % len(shapes), move_idx % len(moves))
    if key in seen:
        old_i, old_top = seen[key]
        delta_i, delta_top = i + 1 - old_i, curr_top - old_top
        m = (BIG_NUM - old_i) // delta_i
        r = (BIG_NUM - old_i) % delta_i
        part2_answer = top[r + old_i] + delta_top * m
        if i+1 >= 2022:
            break
    seen[key] = (i+1, curr_top)


puzzle.answer_a = top[2022]
print('Part1:', puzzle.answer_a)
puzzle.answer_b = part2_answer
print('Part2:', puzzle.answer_b)
