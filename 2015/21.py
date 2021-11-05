from current_puzzle import current_puzzle
from itertools import combinations
import re


def win(boss, you):
    bh = boss[0]
    yh = you[0]
    while True:
        bh -= max(1, you[1] - boss[2])
        if bh <= 0:
            return True
        yh -= max(1, boss[1] - you[2])
        if yh <= 0:
            return False


def rings_stat_sum(comb):
    return tuple(sum(rings[item][j] for item in comb) for j in range(3))


puzzle = current_puzzle()
input_data = puzzle.input_data

boss = list(map(int, re.findall(r'\d+', input_data)))
rings = [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]
armors = [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]

two_rings = map(rings_stat_sum, combinations(range(6), 2))

DAMAGE = 1
ARMOR = 2
COST = 0
max_gold, min_gold = 0, float('inf')
for r in [(0, 0, 0)] + rings + list(two_rings):
    for a in [(0, 0, 0)] + armors:
        for w in weapons:
            gold = r[COST] + w[COST] + a[COST]
            damage = r[DAMAGE] + w[DAMAGE] + a[DAMAGE]
            armor = r[ARMOR] + w[ARMOR] + a[ARMOR]
            if win(boss, [100, damage, armor]):
                min_gold = min(min_gold, gold)
            else:
                max_gold = max(max_gold, gold)

puzzle.answer_a = min_gold
print('Part1:', puzzle.answer_a)
puzzle.answer_b = max_gold
print('Part2:', puzzle.answer_b)
