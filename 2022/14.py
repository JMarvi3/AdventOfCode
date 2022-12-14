from current_puzzle import current_puzzle


def draw_grid(grid):
    for y in range(max_y+3):
        print(''.join(grid.get((x, y), ' ') for x in range(min_x, max_x+1)))


def do_sand(maximum):
    sand = (500, 0)
    possible_move = True
    while possible_move:
        if sand[-1] == maximum:
            break
        possible_move = False
        for pt in [(0, 1), (-1, 1), (1, 1)]:
            new_pt = (sand[0] + pt[0], sand[1] + pt[1])
            if new_pt not in grid:
                sand = new_pt
                possible_move = True
                break
    return sand


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('14.example').read()

grid = dict()
max_y = -float('inf')
for line in input_data.splitlines():
    coords = []
    for coord in line.split(' -> '):
        coords.append(tuple(map(int, coord.split(','))))
    start = coords[0]
    for end in coords[1:]:
        max_y = max(max_y, start[1], end[1])
        move = end
        if start > move:
            start, move = move, start
        x, y = start
        if x == move[0]:
            for y in range(start[1], move[1] + 1):
                grid[(x, y)] = '#'
        else:
            for x in range(start[0], move[0] + 1):
                grid[(x, y)] = '#'
        start = end

min_x, max_x = 500 - max_y - 2, 500 + max_y + 2
grid.update({(x, max_y+2): '#' for x in range(min_x, max_x+1)})
empty_grid_size = len(grid)

while True:
    sand = do_sand(max_y)
    if sand[-1] >= max_y:
        break
    grid[sand] = '.'


puzzle.answer_a = len(grid) - empty_grid_size
print('Part1:', puzzle.answer_a)

while True:
    sand = do_sand(max_y + 1)
    grid[sand] = 'o'
    if sand == (500, 0):
        break

# draw_grid(grid)
puzzle.answer_b = len(grid) - empty_grid_size
print('Part2:', puzzle.answer_b)
