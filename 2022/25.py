from current_puzzle import current_puzzle
import aoc_lib


def from_snafu(s):
    pow = 1
    result = 0
    for c in reversed(s):
        result += digits[c]*pow
        pow *= 5
    return result

def to_snafu(n):
    result = ''
    while n:
        next_digit = from_digits[n % 5]
        n -= digits[next_digit]
        result += next_digit
        assert n % 5 == 0
        n //= 5
    return result[::-1]


digits = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
from_digits = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('25.example').read()

total = sum(map(from_snafu, input_data.splitlines()))
print(to_snafu(total))
puzzle.answer_a = to_snafu(total)
print('Part1:', puzzle.answer_a)
# puzzle.answer_b = None
# print('Part2:', puzzle.answer_b)
