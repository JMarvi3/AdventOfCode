from aocd.models import Puzzle


def calc_steps(jumps, part2=False):
    jumps = list(jumps)
    pc = steps = 0
    while 0 <= pc < len(jumps):
        jump = jumps[pc]
        jumps[pc] += 1 if jump < 3 or not part2 else -1
        steps += 1
        pc += jump
    return steps


data = list(map(int, Puzzle(2017, 5).input_data.splitlines()))

print('Part1:', calc_steps(data))
print('Part2:', calc_steps(data, part2=True))
