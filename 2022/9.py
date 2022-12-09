from current_puzzle import current_puzzle
from aoc_lib import add_pts


def follow(p1, p2):
    while True:
        d = p2[0] - p1[0], p2[1] - p1[1]
        if abs(d[0]) <= 1 and abs(d[1]) <= 1:
            break
        if d[0] != 0:
            p1 = (p1[0] + d[0]//abs(d[0]), p1[1])
        if d[1] != 0:
            p1 = (p1[0], p1[1] + d[1]//abs(d[1]))
    return p1


def do_knots(moves, num_knots):
    move_dirs = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    knots = [(0, 0)] * num_knots
    seen = set([(0, 0)])
    for move, n in moves:
        direction = move_dirs[move]
        for _ in range(int(n)):
            knots[0] = add_pts(knots[0], direction)
            for i in range(1, num_knots):
                knots[i] = follow(knots[i], knots[i - 1])
            seen.add(knots[-1])
    return len(seen)


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('9.example').read()
# input_data = open('9.example2').read()

moves = list(map(str.split, input_data.splitlines()))

# It is possible to do this in one pass by doing part2 and keeping track of knots 2 and 10.

puzzle.answer_a = do_knots(moves, 2)
print('Part1:', puzzle.answer_a)
puzzle.answer_b = do_knots(moves, 10)
print('Part2:', puzzle.answer_b)
