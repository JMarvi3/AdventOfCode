from current_puzzle import current_puzzle
import time


def transpose(grid):
    new_grid = list(map(list, grid))
    for y in range(len(grid)):
        for x in range(len(grid)):
            new_grid[y][x] = grid[x][y]
    return [''.join(line) for line in new_grid]


def flip_vertical(grid):
    return [grid[y] for y in range(len(grid)-1, -1, -1)]


def split(grid):
    old_len = len(grid)
    if old_len <= 3:
        return [[grid]]
    new_len = 2 if old_len % 2 == 0 else 3
    new_size = old_len // new_len
    new_grid = [[[] for _ in range(new_size)] for _ in range(new_size)]
    for i, line in enumerate(grid):
        y = i // new_len
        for j in range(0, old_len, new_len):
            x = j // new_len
            new_grid[y][x].append(line[j:j + new_len])
    return new_grid


def join(grid):
    size = len(grid)
    inner_size = len(grid[0][0])
    new_grid = []
    for i in range(size):
        row = [''] * inner_size
        for j in range(size):
            for k in range(inner_size):
                row[k] += grid[i][j][k]
        new_grid.extend(row)
    return new_grid


def process(grid):
    grid = split(grid)
    for y in range(len(grid)):
        for x in range(len(grid)):
            grid[y][x] = patterns['/'.join(grid[y][x])].split('/')
    return join(grid)


start = time.perf_counter_ns()

patterns = dict()
for line in current_puzzle().input_data.splitlines():
    left, right = line.split(" => ")
    patt = left.split('/')
    for _ in range(4):
        patt = transpose(patt)
        patterns['/'.join(patt)] = right
        patt = flip_vertical(patt)
        patterns['/'.join(patt)] = right

grid = ".#./..#/###".split('/')
for _ in range(5):
    grid = process(grid)

print('Part1:', ''.join(grid).count('#'))

for _ in range(13):
    grid = process(grid)
print('Part2:', ''.join(grid).count('#'))

print(f"Elapsed time: {(time.perf_counter_ns()-start)/1000000:.2f}ms")
