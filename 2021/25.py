from current_puzzle import current_puzzle


def draw_cucumbers(east, south, width, length):
    for y in range(length):
        print(''.join('>' if (x, y) in east else 'v' if (x, y) in south else '.' for x in range(width)))


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('25.example').read()

lines = input_data.splitlines()
length, width = len(lines), len(lines[0])

east = set()
south = set()
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c == '>':
            east.add((x, y))
        elif c == 'v':
            south.add((x, y))

done = False
steps = 0
while not done:
    steps += 1
    done = True
    new_east = set()
    for x, y in east:
        dest_x = (x + 1) % width
        if (dest_x, y) not in east and (dest_x, y) not in south:
            new_east.add((dest_x, y))
            done = False
        else:
            new_east.add((x, y))
    east = new_east
    new_south = set()
    for x, y in south:
        dest_y = (y + 1) % length
        if (x, dest_y) not in east and (x, dest_y) not in south:
            new_south.add((x, dest_y))
            done = False
        else:
            new_south.add((x, y))
    south = new_south

puzzle.answer_a = steps
print('Part1:', puzzle.answer_a)
# puzzle.answer_b = None
# print('Part2:', puzzle.answer_b)
