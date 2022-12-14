from copy import deepcopy

from current_puzzle import current_puzzle
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('14.example').read()

max_y = 0
grid = dict()
lines = []
for line in input_data.splitlines():
    coords = []
    for coord in line.split(' -> '):
        coords.append(tuple(map(int, coord.split(','))))
    start = coords[0]
    for end in coords[1:]:
        move = end
        if start > move:
            start, move = move, start
        x, y = start
        if x == move[0]:
            for y in range(start[1], move[1]+1):
                grid[(x, y)] = '#'
        else:
            for x in range(start[0], move[0]+1):
                grid[(x, y)] = '#'
        start = end
    lines.append(coords)
min_x, max_x = min(g[0] for g in grid), max(g[0] for g in grid)
min_y, max_y = min(g[1] for g in grid), max(g[1] for g in grid)

def draw_grid(grid):
    for y in range(min_y-5, max_y+3):
        print(''.join(grid.get((x,y), '.') for x in range(min_x-10, max_x+10)))
    print('------------------------')

def do_sand(maximum):
    sand = (500, 0)
    possible_move = True
    while possible_move:
        if sand[-1] == maximum:
            break
        possible_move = False
        for pt in [(0,1), (-1,1), (1,1)]:
            new_pt = aoc_lib.add_pts(sand, pt)
            if new_pt not in grid:
                sand = new_pt
                possible_move = True
                break
    return sand

moves = 0
while True:
    sand = do_sand(max_y)
    grid[sand] = 'o'
    moves += 1
    if sand[-1] >= max_y:
        break

puzzle.answer_a = moves - 1
print('Part1:', puzzle.answer_a)

moves -= 1
del grid[sand]
while True:
    sand = do_sand(max_y+1)
    grid[sand] = 'o'
    moves += 1
    if sand == (500, 0):
        break

puzzle.answer_b = moves
print('Part2:', puzzle.answer_b)
# print(puzzle.incorrect_answers_b)