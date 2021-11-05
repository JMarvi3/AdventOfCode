from current_puzzle import current_puzzle
puzzle = current_puzzle()
input_data = puzzle.input_data

part2 = -1
floor = 0
for i, c in enumerate(input_data):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -= 1
        if floor == -1 and part2 == -1:
            part2 = i + 1

puzzle.answer_a = floor
print('part 1:', puzzle.answer_a)
puzzle.answer_b = part2
print('part 2:', puzzle.answer_b)
