from current_puzzle import current_puzzle
from collections import Counter
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('14.example').read()


def get_counts(start, rule_pairs, iters):
    pairs = Counter()
    for i in range(0, len(start) - 1):
        pairs[start[i:i + 2]] += 1

    for _ in range(iters):
        new_pairs = Counter()
        for pair, count in pairs.items():
            for result in rule_pairs[pair]:
                new_pairs[result] += count
        pairs = new_pairs

    c = Counter(start[0] + start[-1])
    for pair, count in pairs.items():
        c[pair[0]] += count
        c[pair[1]] += count
    c = c.most_common()
    return (c[0][1] - c[-1][1])//2


start = input_data.splitlines()[0]
rules = dict([tuple(line.split(' -> ')) for line in input_data.splitlines()[2:]])
rule_pairs = {rule: (rule[0] + rules[rule], rules[rule] + rule[1]) for rule in rules}

puzzle.answer_a = get_counts(start, rule_pairs, 10)
print('Part1:', puzzle.answer_a)

puzzle.answer_b = get_counts(start, rule_pairs, 40)
print('Part2:', puzzle.answer_b)
