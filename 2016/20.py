from aocd.models import Puzzle

bans = [list(map(int, line.split('-'))) for line in Puzzle(2016, 20).input_data.splitlines()]
bans.sort()

start = 0
count = 0
for ban in bans:
    if start < ban[0]:
        if count == 0:
            print('part1', start)
        count += ban[0] - start
        start = ban[1] + 1
    elif start <= ban[1]:
        start = ban[1] + 1

print('part2:', count)
