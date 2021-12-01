from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data


increasing_count = lambda data: sum(data[i] > data[i-1] for i in range(1, len(data)))

depths = list(map(int, input_data.splitlines()))
puzzle.answer_a = increasing_count(depths)
print('Part1:', puzzle.answer_a)

sums = list(sum(depths[i:i+3]) for i in range(len(depths)-2))
puzzle.answer_b = increasing_count(sums)
print('Part2:', puzzle.answer_b)

print(int(puzzle.answer_b) - int(puzzle.answer_a))

print(sum(depths[i] > depths[i-3] for i in range(3, len(depths))))
