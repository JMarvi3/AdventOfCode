from aocd.models import Puzzle


def get_code(start, buttons, lines):
    x, y = start
    code = ''
    for line in lines:
        for c in line:
            new_x, new_y = x, y
            if c == 'U':
                new_y -= 1
            elif c == 'L':
                new_x -= 1
            elif c == 'D':
                new_y += 1
            elif c == 'R':
                new_x += 1
            if (new_x, new_y) in buttons:
                x, y = new_x, new_y
        code += buttons[(x, y)]
    return code


def make_dict(keypad: str):
    rows = keypad.splitlines()
    d = dict()
    five_pos = None
    for y in range(len(rows)):
        for x in range(len(rows[0])):
            if rows[y][x] != ' ':
                d[(x, y)] = rows[y][x]
            if rows[y][x] == '5':
                five_pos = (x, y)
    return five_pos, d


lines = Puzzle(2016, 2).input_data.splitlines()
print('part1:', get_code(*make_dict('123\n456\n789'), lines))
print('part2:', get_code(*make_dict('  1  \n 234 \n56789\n ABC \n  D  '), lines))
