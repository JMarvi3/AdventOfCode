import itertools
from current_puzzle import current_puzzle

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n'
#input_data = open('8.example').read()

count = 0
for line in input_data.splitlines():
    count += sum(len(word) in {2, 3, 4, 7} for word in line.split(' | ')[1].split())

puzzle.answer_a = count
print('Part1:', puzzle.answer_a)


def convert(word, mapping):
    return ''.join(sorted(mapping[c] for c in word))


displays = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg',
            6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg'}
numbers = {v: k for k, v in displays.items()}
mappings = [dict(zip('abcdefg', perm)) for perm in itertools.permutations('abcdefg')]

total = 0
for line in input_data.splitlines():
    parts = line.split(' | ')
    words = [''.join(sorted(word)) for word in parts[0].split()]
    mapping = next(mapping for mapping in mappings if all(convert(word, mapping) in numbers for word in words))
    digits = [numbers[convert(word, mapping)] for word in parts[1].split()]
    total += int(''.join(map(str, digits)))

puzzle.answer_b = total
print('Part2:', puzzle.answer_b)

