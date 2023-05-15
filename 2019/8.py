from current_puzzle import current_puzzle
import aoc_lib
from collections import Counter
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data


ROWS, COLS = 6, 25
LAYER_SIZE = ROWS * COLS
layers = [input_data[start:start+LAYER_SIZE] for start in range(0, len(input_data), LAYER_SIZE)]
min_layer = min(layers, key=lambda layer: layer.count('0'))
counts = Counter(min_layer)
puzzle.answer_a = counts['1'] * counts['2']
print('Part1:', puzzle.answer_a)

final_picture = ['2'] * LAYER_SIZE
for i, pixels in enumerate(zip(*layers)):
    for pixel in pixels:
        if pixel != '2':
            final_picture[i] = pixel
            break

final_picture = ''.join('*' if pixel == '1' else ' ' for pixel in final_picture)
for y in range(6):
    print(final_picture[y*COLS:y*COLS+COLS])

# puzzle.answer_b = None
# print('Part2:', puzzle.answer_b)
