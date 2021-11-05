import re
import json
from current_puzzle import current_puzzle


def object_sum(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(object_sum(c) for c in obj)
    elif isinstance(obj, dict) and 'red' not in obj.values():
        return sum(object_sum(value) for value in obj.values())
    else:
        return 0


puzzle = current_puzzle()
input_data = puzzle.input_data

total = sum(map(int, re.findall(r"-?\d+", input_data)))

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

total = sum(object_sum(json.loads(line)) for line in input_data.splitlines())

puzzle.answer_b = total
print('Part2:', puzzle.answer_b)

