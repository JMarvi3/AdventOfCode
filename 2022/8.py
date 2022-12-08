from current_puzzle import current_puzzle

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('8.example').read()
trees = dict()
for y, row in enumerate(input_data.splitlines()):
    for x, col in enumerate(row):
        trees[(x, y)] = int(col)

visible = set()
max_x, max_y = x, y
for y in range(max_y + 1):
    max_v = -1
    for x in range(max_x + 1):
        if trees[(x, y)] > max_v:
            max_v = trees[(x, y)]
            visible.add((x, y))
    max_v = -1
    for x in range(max_x, -1, -1):
        if trees[(x, y)] > max_v:
            max_v = trees[(x, y)]
            visible.add((x, y))

for x in range(max_x + 1):
    max_v = -1
    for y in range(max_y, -1, -1):
        if trees[(x, y)] > max_v:
            max_v = trees[(x, y)]
            visible.add((x, y))
    max_v = -1
    for y in range(max_y + 1):
        if trees[(x, y)] > max_v:
            max_v = trees[(x, y)]
            visible.add((x, y))

# for y in range(max_y+1):
#     print(''.join('*' if (x,y) in visible else '.' for x in range(max_x+1)))

puzzle.answer_a = len(visible)
print('Part1:', puzzle.answer_a)


def ray(x, y):
    score = 1
    height = trees[(x, y)]
    max_range = 0
    for y1 in range(y - 1, -1, -1):
        max_range += 1
        if trees[(x, y1)] >= height:
            break
    score *= max_range
    max_range = 0
    for y1 in range(y + 1, max_y + 1):
        max_range += 1
        if trees[(x, y1)] >= height:
            break
    score *= max_range
    max_range = 0
    for x1 in range(x - 1, -1, -1):
        max_range += 1
        if trees[(x1, y)] >= height:
            break
    score *= max_range
    max_range = 0
    for x1 in range(x + 1, max_x + 1):
        max_range += 1
        if trees[(x1, y)] >= height:
            break
    score *= max_range
    return score


max_score = max(ray(x, y) for x in range(1, max_x) for y in range(1, max_y))

puzzle.answer_b = max_score
print('Part2:', puzzle.answer_b)
