from current_puzzle import current_puzzle

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('8.example').read()
trees = dict()
for y, row in enumerate(input_data.splitlines()):
    for x, col in enumerate(row):
        trees[(x, y)] = int(col)

max_x, max_y = x, y


def scan(x_min, x_max, x_stride, y_min, y_max, y_stride):
    max_v = -1
    for x in range(x_min, x_max, x_stride):
        for y in range(y_min, y_max, y_stride):
            if trees[(x,y)] > max_v:
                max_v = trees[(x, y)]
                visible.add((x, y))


visible = set()
for y in range(max_y+1):
    scan(0, max_x+1, 1, y, y+1, 1)
    scan(max_x, -1, -1, y, y+1, 1)
for x in range(max_x+1):
    scan(x, x+1, 1, 0, max_y+1, 1)
    scan(x, x+1, 1, max_y, -1, -1)

puzzle.answer_a = len(visible)
print('Part1:', puzzle.answer_a)


def ray(x, y):
    def look_out(x_min, x_max, x_stride, y_min, y_max, y_stride):
        max_range = 0
        for x1 in range(x_min, x_max, x_stride):
            for y1 in range(y_min, y_max, y_stride):
                max_range += 1
                if trees[(x1, y1)] >= height:
                    return max_range
        return max_range

    score = 1
    height = trees[(x, y)]
    score *= look_out(x, x+1, 1, y-1, -1, -1)
    score *= look_out(x, x+1, 1, y+1, max_y+1, 1)
    score *= look_out(x-1, -1, -1, y, y+1, 1)
    score *= look_out(x+1, max_x+1, 1, y, y+1, 1)
    return score


max_score = max(ray(x, y) for x in range(1, max_x) for y in range(1, max_y))

puzzle.answer_b = max_score
print('Part2:', puzzle.answer_b)
