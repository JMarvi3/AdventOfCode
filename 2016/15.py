from aocd.models import Puzzle
import re


def find_time(discs):
    time = 0
    prev_period = 1
    for disc in discs:
        while (time + disc[0] + disc[3]) % disc[1] != 0:
            time += prev_period
        prev_period *= disc[1]
    return time


num_pat = re.compile(r'\d+')

test_s = 'Disc #1 has 5 positions; at time=0, it is at position 4.\n' \
         'Disc #2 has 2 positions; at time=0, it is at position 1. '
s = Puzzle(2016, 15).input_data
discs = [list(map(int, num_pat.findall(line))) for line in s.splitlines()]

print('part1:', find_time(discs))
print('part2:', find_time(discs + [[discs[-1][0] + 1, 11, 0, 0]]))
