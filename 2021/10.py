from current_puzzle import current_puzzle
import statistics

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('10.example').read()

opp = dict(zip('([{<', ')]}>'))
part1_scores = dict(zip(')]}>', [3, 57, 1197, 25137]))
part2_scores = dict(zip(')]}>', [1, 2, 3, 4]))
incomplete_line_scores = []
part1_total = 0
for line in input_data.splitlines():
    stack = []
    for c in line:
        if c in '([{<':
            stack.append(opp[c])
        else:
            s = stack.pop()
            if s != c:
                part1_total += part1_scores[c]
                break
    else:
        if stack:
            total = 0
            for c in stack[::-1]:
                total = total * 5 + part2_scores[c]
            incomplete_line_scores.append(total)

puzzle.answer_a = part1_total
print('Part1:', puzzle.answer_a)

puzzle.answer_b = int(statistics.median(incomplete_line_scores))
print('Part2:', puzzle.answer_b)
