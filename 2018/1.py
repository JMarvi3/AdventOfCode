from aocd.models import Puzzle

deltas = list(map(int, Puzzle(2018, 1).input_data.splitlines()))

print('Part1:', sum(deltas))

seen = set()
freq = pos = 0
while freq not in seen:
    seen.add(freq)
    freq += deltas[pos]
    pos = (pos + 1) % len(deltas)

print('Part2:', freq)
