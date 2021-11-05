from current_puzzle import current_puzzle
import re

puzzle = current_puzzle()
input_data = puzzle.input_data

row, col = map(int, re.findall(r'\d+', input_data))
diag = row + col - 1            # move down until col == 1
count = (diag - 1) * diag // 2 + col - 1  # move back up

num = 20151125
a = 252533
b = 33554393
puzzle.answer_a = (num * pow(a, count, b)) % b
print('Part1:', puzzle.answer_a)
