from collections import defaultdict, Counter
from aocd.models import Puzzle

counters = defaultdict(Counter)
for line in Puzzle(2016, 6).input_data.splitlines():
    for i, c in enumerate(line):
        counters[i][c] += 1

print(''.join(counters[i].most_common()[0][0] for i in range(len(counters))))
print(''.join(counters[i].most_common()[-1][0] for i in range(len(counters))))