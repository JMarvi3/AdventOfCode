import re
import time
from z3 import Optimize, If, Sum, Ints, sat
from current_puzzle import current_puzzle


def dist(pt1, pt2):
    return sum(abs(pt1[i] - pt2[i]) for i in range(3))


def zdist(pt1, pt2):
    return Sum([If(pt1[i] < pt2[i], pt2[i] - pt1[i], pt1[i] - pt2[i]) for i in range(3)])


pat = re.compile(r"-?\d+")
puzzle = current_puzzle()
input_data = puzzle.input_data

bots = list(tuple(map(int, pat.findall(line))) for line in input_data.splitlines())

start = time.perf_counter()

_, max_bot = max((bot[3], bot) for bot in bots)

puzzle.answer_a = sum(dist(bot, max_bot) < max_bot[3] for bot in bots)
print('Part1:', puzzle.answer_a)

o = Optimize()
x, y, z, dist_from_zero = Ints("x y z dist_from_zero")
o.add(dist_from_zero == zdist((x, y, z), (0, 0, 0)))
o.maximize(Sum([If(zdist(bot, (x, y, z)) <= bot[3], 1, 0) for bot in bots]))
o.minimize(dist_from_zero)
assert o.check() == sat

puzzle.answer_b = o.model().eval(dist_from_zero)
print('Part2:', puzzle.answer_b)

print(f"Elapsed time: {time.perf_counter()-start:.2f}s")
