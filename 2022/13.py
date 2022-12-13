from current_puzzle import current_puzzle

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('13.example').read()

def compare(left, right):
    if type(left) == int and type(right) == int:
        return left - right
    if type(left) == int:
        left = [left]
    if type(right) == int:
        right = [right]
    for i in range(max(len(left), len(right))):
        if i == len(left):
            return -1
        if i == len(right):
            return 1
        test = compare(left[i], right[i])
        if test == 0:
            continue
        return test
    return 0


part1 = 0
for i, line in enumerate(input_data.split('\n\n')):
    left, right = map(eval, line.splitlines())
    test = compare(left, right) <= 0
    if test:
        part1 += i+1
puzzle.answer_a = part1
print('Part1:', puzzle.answer_a)

part2_data = list(map(eval, (input_data.replace('\n\n', '\n') + '\n[[2]]\n[[6]]').splitlines()))
while True:
    out_of_order = False
    for i in range(1, len(part2_data)):
        if compare(part2_data[i-1], part2_data[i]) > 0:
            part2_data[i-1], part2_data[i] = part2_data[i], part2_data[i-1]
            out_of_order = True
    if not out_of_order:
        break

indexes = []
for i, l in enumerate(part2_data):
    if l in [[[2]], [[6]]]:
        indexes.append(i+1)

puzzle.answer_b = indexes[0] * indexes[1]
print('Part2:', puzzle.answer_b)
