from current_puzzle import current_puzzle
import aoc_lib


def priority(item):
    if item > 'Z':
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
elves = input_data.split('\n')

total = 0
for line in elves:
    total += priority(set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop())

part2_total = 0
for i in range(0, len(elves), 3):
    items1, items2, items3 = elves[i], elves[i+1], elves[i+2]
    part2_total += priority(set(items1).intersection(set(items2).intersection(set(items3))).pop())

puzzle.answer_a = total
print('Part1:', puzzle.answer_a)

puzzle.answer_b = part2_total
print('Part2:', puzzle.answer_b)
