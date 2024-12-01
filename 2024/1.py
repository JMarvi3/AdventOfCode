from current_puzzle import current_puzzle

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('1.example').read()

data = [list(map(int, line.split())) for line in input_data.splitlines()]
data = list(zip(*data))
data = list(map(sorted, data))
data_2 = data[::]
data = list(zip(*data))

total_distance = sum(map(lambda elem: abs(elem[0]-elem[1]), data))
print(total_distance)
# puzzle.answer_a = total_distance
print('Part1:', puzzle.answer_a)

similarity_score = 0
for num in data_2[0]:
    similarity_score += num * data_2[1].count(num)

print(similarity_score)
puzzle.answer_b = similarity_score
print('Part2:', puzzle.answer_b)
