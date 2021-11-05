import itertools
from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

containers = list(map(int, input_data.splitlines()))

count = min_count = 0
for i in range(len(containers)):
    local_count = 0
    for comb in itertools.combinations(containers, i+1):
        if sum(comb) == 150:
            local_count += 1
    count += local_count
    if min_count == 0:
        min_count = local_count

puzzle.answer_a = count
print('Part1:', puzzle.answer_a)
puzzle.answer_b = min_count
print('Part2:', puzzle.answer_b)
