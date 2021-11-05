from aocd.models import Puzzle

input_data = Puzzle(2017, 24).input_data.splitlines()
#input_data = ["0/2", "2/2", "2/3", "3/4", "3/5", "0/1", "10/1", "9/10"]
connectors = [tuple(map(int, line.split('/'))) for line in input_data]


def best_bridge(left, used: set, length=0, strength=0):
    global best_long, max_length, best_abs
    if strength > best_abs:
        best_abs = strength
        # print('abs', length, strength)
    if length >= max_length:
        max_length = length
        if strength > best_long:
            best_long = strength
            # print('long', length, strength)
    for connector in connectors:
        if connector not in used:
            right = None
            if connector[0] == left:
                right = connector[1]
            elif connector[1] == left:
                right = connector[0]
            if right is not None:
                used.add(connector)
                best_bridge(right, used, length+1, strength + sum(connector))
                used.remove(connector)


best_abs = best_long = max_length = 0
best_bridge(0, set())
print('Part1:', best_abs)
print('Part2:', best_long)
