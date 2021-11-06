from current_puzzle import current_puzzle


def do_pots(pots, rules):
    new_pots = pots.copy()
    for i in range(min(pots) - 1, max(pots) + 2):
        match = ''.join(pots.get(j, '.') for j in range(i - 2, i + 3))
        pot = rules.get(match, '.')
        if pot == '#':
            new_pots[i] = pot
        elif i in pots:
            del new_pots[i]
    return new_pots


puzzle = current_puzzle()
input_data = puzzle.input_data

lines = input_data.splitlines()
# lines = open('12.example').readlines()

initial_pots = {k: v for k, v in enumerate(lines[0].split(': ')[1]) if v == '#'}

rules = dict()
for line in lines[2:]:
    left, right = line.strip().split(' => ')
    rules[left] = right

pots = initial_pots.copy()
for n in range(20):
    pots = do_pots(pots, rules)

puzzle.answer_a = sum(pots)
print(puzzle.answer_a)

pots = initial_pots.copy()
prev = sum(pots)
diff = prev_diff = 0
for n in range(2000):
    pots = do_pots(pots, rules)
    new_sum = sum(pots)
    diff = new_sum - prev
    if diff == prev_diff:
        break
    prev, prev_diff = new_sum, diff

puzzle.answer_b = new_sum + (50000000000-n-1)*diff
print(puzzle.answer_b)
