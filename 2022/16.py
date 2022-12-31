from functools import cache
import re
from current_puzzle import current_puzzle


@cache
def solve(valve: str, open_valves: frozenset[str], minutes_left: int, elephant=False):
    if minutes_left == 0:
        return solve('AA', open_valves, 26, False) if elephant else 0
    answer = 0
    flow, other_valves = valves[valve]
    if flow > 0 and valve not in open_valves:
        answer = (minutes_left - 1) * flow + solve(valve, open_valves.union([valve]), minutes_left - 1, elephant)
    for other_valve in other_valves:
        answer = max(answer, solve(other_valve, open_valves, minutes_left - 1, elephant))
    return answer


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('16.example').read()

pat = re.compile(r"Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)")
valves = dict()
max_pressure = 0
for line in input_data.splitlines():
    name, flow, to = pat.match(line).group(1, 2, 3)
    flow, to = int(flow), to.split(', ')
    valves[name] = (flow, to)
    max_pressure += flow

# print(solve('AA', frozenset(), 30))
# print()
puzzle.answer_a = solve('AA', frozenset(), 30)
print('Part1:', puzzle.answer_a)
puzzle.answer_b = solve('AA', frozenset(), 26, True)
print('Part2:', puzzle.answer_b)
