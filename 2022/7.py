from current_puzzle import current_puzzle
from collections import defaultdict

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

dirs = defaultdict(int)
curr_path = ['']
for line in input_data.splitlines():
    line_parts = line.split()
    if line_parts[0] == '$':
        if line_parts[1] == 'cd':
            file = line.split()[2]
            if file == '..' and len(curr_path) > 1:
                curr_path.pop(-1)
            elif file == '/':
                curr_path = ['']
            else:
                curr_path.append(curr_path[-1] + '/' + file)
    else:
        size, file = line_parts
        if size.isnumeric():
            size = int(size)
            for path in curr_path:
                dirs[path] += size

part1 = sum(v for v in dirs.values() if v <= 100_000)

puzzle.answer_a = part1
print('Part1:', puzzle.answer_a)

unused = 70_000_000 - dirs['']
needed = 30_000_000 - unused
part2 = min(size for size in dirs.values() if size >= needed)

puzzle.answer_b = part2
print('Part2:', puzzle.answer_b)
