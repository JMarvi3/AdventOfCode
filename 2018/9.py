from current_puzzle import current_puzzle
import re
from collections import deque

puzzle = current_puzzle()
input_data = puzzle.input_data
num_players, last_marble = map(int, re.findall(r"(\d+)", input_data))
#num_players, last_marble = 30, 5807

scores = [0] * num_players
q = deque([0])
for i in range(1, last_marble*100 + 1):
    if i % 23:
        q.append(i)
        q.rotate(-1)
    else:
        q.rotate(8)
        scores[i % num_players] += q.pop() + i
        q.rotate(-2)
    if i == last_marble:
        part1_answer = max(scores)

puzzle.answer_a = part1_answer
print(puzzle.answer_a)
puzzle.answer_b = max(scores)
print(puzzle.answer_b)
