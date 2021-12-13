from current_puzzle import current_puzzle
import parse

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('13.example').read()


def draw_field(field):
    max_x, max_y = map(max, zip(*field))
    for y in range(max_y + 1):
        print(''.join('*' if (x, y) in field else ' ' for x in range(max_x + 1)))


def fold(field, axis, fold_line):
    if axis == 'x':
        return set((x, y) if x <= fold_line else (fold_line*2 - x, y) for x, y in field)
    else:
        return set((x, y) if y <= fold_line else (x, fold_line*2 - y) for x, y in field)


dots, instructions = map(str.splitlines, input_data.split('\n\n'))
field = set(tuple(map(int, dot.split(','))) for dot in dots)
instructions = [tuple(parse.parse("fold along {}={:d}", instruction)) for instruction in instructions]

puzzle.answer_a = len(fold(field, *instructions[0]))
print('Part1:', puzzle.answer_a)

for instruction in instructions:
    field = fold(field, *instruction)
draw_field(field)
# puzzle.answer_b = None
# print('Part2:', puzzle.answer_b)
