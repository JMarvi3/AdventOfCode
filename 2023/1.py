import regex
from current_puzzle import current_puzzle
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

total = 0
for line in input_data.splitlines():
    digits = regex.findall(r"[0-9]", line)
    total += int(digits[0])*10 + int(digits[-1])

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)


m = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
     'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
pattern = '|'.join(m.keys())
total = 0
for line in input_data.splitlines():
    digits = [m[digit] for digit in regex.findall(pattern, line, overlapped=True)]
    total += digits[0] * 10 + digits[-1]

puzzle.answer_b = total
print('Part2:', puzzle.answer_b)