from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

paper = ribbon = 0
for package in input_data.splitlines():
    l, w, h = sorted(map(int, package.split('x')))
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    ribbon += 2*l + 2*w + l*w*h


puzzle.answer_a = paper
print('Part1:', puzzle.answer_a)
puzzle.answer_b = ribbon
print('Part2:', puzzle.answer_b)
