from current_puzzle import current_puzzle
import re

puzzle = current_puzzle()
input_data = puzzle.input_data

package = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
           'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

pat = re.compile(r'(\w+): (\d+)')
aunts = []
for i, line in enumerate(input_data.splitlines()):
    right_aunt = True
    aunt = dict()
    for category, n in pat.findall(line):
        aunt[category] = int(n)
        if package[category] != int(n):
            right_aunt = False
    aunts.append(aunt)
    if right_aunt:
        sue = i+1

puzzle.answer_a = sue
print('Part1:', puzzle.answer_a)

for i, aunt in enumerate(aunts):
    right_aunt = True
    for category in aunt:
        if category == 'cats' or category == 'trees':
            if aunt[category] <= package[category]:
                right_aunt = False
                break
        elif category == 'pomeranians' or category == 'goldfish':
            if aunt[category] >= package[category]:
                right_aunt = False
                break
        elif aunt[category] != package[category]:
            right_aunt = False
            break
    if right_aunt:
        real_sue = i+1
        break

puzzle.answer_b = real_sue
print('Part2:', puzzle.answer_b)
