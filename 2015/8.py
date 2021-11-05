import re
from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

decoded_diff = encoded_diff = 0

for line in input_data.splitlines():
    # print(line, end=' , ')
    line = line.strip()
    decoded_diff += len(re.findall(r'\\x[0-9a-fA-F]{2}', line)) * 3 + len(re.findall(r'(\\")|(\\\\)', line)) + 2
    encoded_diff += len(re.findall(r'[\\"]', line)) + 2

puzzle.answer_a = decoded_diff
print('Part1:', puzzle.answer_a)
puzzle.answer_b = encoded_diff
print('Part2:', puzzle.answer_b)
