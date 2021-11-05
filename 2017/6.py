from aocd.models import Puzzle

blocks = list(map(int, Puzzle(2017, 6).input_data.split()))

n = len(blocks)
steps = 0
seen = {tuple(blocks): 0}

while True:
    index = blocks.index(max(blocks))
    realloc, blocks[index] = blocks[index], 0
    for i in range(1, realloc+1):
        blocks[(index + i) % n] += 1
    steps += 1
    t = tuple(blocks)
    if t in seen:
        break
    seen[t] = steps

print('Part1:', steps)
print('Part2:', steps-seen[t])
