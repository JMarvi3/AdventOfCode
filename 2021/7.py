from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

positions = list(map(int, input_data.split(',')))
max_pos = max(positions)

puzzle.answer_a = min(sum(abs(dest - pos) for pos in positions) for dest in range(max_pos+1))
print('Part1:', puzzle.answer_a)

fuel_used = lambda dist: dist * (dist + 1) // 2
puzzle.answer_b = min(sum(fuel_used(abs(dest - pos)) for pos in positions) for dest in range(max_pos+1))
print('Part2:', puzzle.answer_b)
