from current_puzzle import current_puzzle
from itertools import combinations
from functools import reduce
from operator import mul


def calc_min_qe(target):
    for n in range(len(packages)):
        qes = [reduce(mul, comb, 1) for comb in combinations(packages, n+1) if sum(comb) == target]
        if qes:
            return min(qes)


puzzle = current_puzzle()
input_data = puzzle.input_data
packages = list(map(int, input_data.splitlines()))

puzzle.answer_a = calc_min_qe(sum(packages)//3)
print('Part1:', puzzle.answer_a)
puzzle.answer_b = calc_min_qe(sum(packages)//4)
print('Part2:', puzzle.answer_b)
