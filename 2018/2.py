from aocd.models import Puzzle
from collections import Counter

boxes = sorted(Puzzle(2018, 2).input_data.splitlines())

two = three = 0
for box in boxes:
    box_counter = Counter(box)
    if 2 in Counter(box).values():
        two += 1
    if 3 in Counter(box).values():
        three += 1
print('Part1:', two*three)

n = len(boxes[0])
answer = ''
for i in range(1, len(boxes)):
    same = []
    for j in range(n):
        if boxes[i][j] == boxes[i-1][j]:
            same.append(boxes[i][j])
    if len(same) == n - 1:
        answer = ''.join(same)
        break
print('Part2:', answer)

