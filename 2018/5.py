from aocd.models import Puzzle


def react(line: str, unit=''):
    left = []
    for c in line:
        if left and left[-1] != c and c.upper() == left[-1].upper():
            left.pop()
        elif c.lower() != unit:
            left.append(c)
    return len(left)


input_data = Puzzle(2018, 5).input_data
print('Part1:', react(input_data))
print('Part2:', min(react(input_data, chr(unit)) for unit in range(ord('a'), ord('z')+1)))
