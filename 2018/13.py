from current_puzzle import current_puzzle


def find_collision(carts, tracks, part2=False):
    while len(carts) > 1:
        for pt in sorted(carts.keys()):
            if pt not in carts:
                continue
            curr_dir, state = carts[pt]
            del carts[pt]
            pt = (pt[0] + dir_deltas[curr_dir][0], pt[1] + dir_deltas[curr_dir][1])
            if pt in carts:
                if not part2:
                    return pt
                del carts[pt]
                continue
            c = tracks.get(pt, ' ')
            if c == '/':
                curr_dir = (curr_dir + (1 if curr_dir in [0, 2] else -1)) % 4
            elif c == '\\':
                curr_dir = (curr_dir - (1 if curr_dir in [0, 2] else -1)) % 4
            elif c == '+':
                if state == 0:
                    curr_dir = (curr_dir - 1) % 4
                elif state == 2:
                    curr_dir = (curr_dir + 1) % 4
                state = (state + 1) % 3
            carts[pt] = (curr_dir, state)
    return next(cart for cart in carts)


puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('13.example').read()

cart_dirs = '^>v<'
dir_deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
carts = dict()
tracks = dict()
for y, line in enumerate(input_data.splitlines()):
    for x, c in enumerate(line.rstrip()):
        if c in cart_dirs:
            carts[(x, y)] = (cart_dirs.index(c), 0)
        else:
            tracks[(x, y)] = c


x, y = find_collision(carts.copy(), tracks)
# print(x, y)
puzzle.answer_a = f"{x},{y}"
print('Part1:', puzzle.answer_a)

x, y = find_collision(carts.copy(), tracks, part2=True)
# print(x, y)
puzzle.answer_b = f"{x},{y}"
print('Part2:', puzzle.answer_b)
