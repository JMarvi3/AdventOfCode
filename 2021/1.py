from current_puzzle import current_puzzle


def increasing_count(data):
    return sum(data[i] > data[i - 1] for i in range(1, len(data)))


puzzle = current_puzzle()
input_data = puzzle.input_data
depths = list(map(int, input_data.splitlines()))

puzzle.answer_a = increasing_count(depths)
print('Part1:', puzzle.answer_a)

sums = list(sum(depths[i:i + 3]) for i in range(len(depths) - 2))
puzzle.answer_b = increasing_count(sums)
print('Part2:', puzzle.answer_b)

# this occurred to me later
part_a, part_b = (sum(a < b for a, b in zip(depths, depths[i:])) for i in (1, 3))
print(part_a, part_b)
