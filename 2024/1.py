from current_puzzle import current_puzzle
from collections import Counter

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('1.example').read()

data = [map(int, line.split()) for line in input_data.splitlines()]
data = list(map(sorted, zip(*data)))
total_distance = sum(abs(a-b) for a, b in zip(*data))

print(total_distance)
puzzle.answer_a = total_distance
print('Part1:', puzzle.answer_a)

counts = Counter(data[1])
similarity_score = sum(num*counts[num] for num in data[0])

print(similarity_score)
puzzle.answer_b = similarity_score
print('Part2:', puzzle.answer_b)
