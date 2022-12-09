from current_puzzle import current_puzzle


def adjust(p1, p2):
    p1 = list(p1)
    while True:
        d = p2[0] - p1[0], p2[1] - p1[1]
        if sorted(map(abs, d))[1] <= 1:
            break
        if d[0] == 0:
            p1[1] += d[1]//abs(d[1])
        elif d[1] == 0:
            p1[0] += d[0]//abs(d[0])
        else:
            p1 = p1[0] + d[0]//abs(d[0]), p1[1] + d[1]//abs(d[1])
    return tuple(p1)


def do_knots(moves, num_knots):
    knots = [(0, 0)] * num_knots
    seen = set([(0, 0)])
    for move, n in moves:
        for _ in range(int(n)):
            head = knots[0]
            if move == 'U':
                head = head[0], head[1] - 1
            elif move == 'D':
                head = head[0], head[1] + 1
            elif move == 'L':
                head = head[0] - 1, head[1]
            elif move == 'R':
                head = head[0] + 1, head[1]
            knots[0] = head
            for i in range(1, num_knots):
                knots[i] = adjust(knots[i], knots[i - 1])
            seen.add(knots[-1])
    return len(seen)


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('9.example').read()
# input_data = open('9.example2').read()

moves = list(map(str.split, input_data.splitlines()))

puzzle.answer_a = do_knots(moves, 2)
print('Part1:', puzzle.answer_a)
puzzle.answer_b = do_knots(moves, 10)
print('Part2:', puzzle.answer_b)
