from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

nice = 0
for s in input_data.splitlines():
    vowels = 0
    has_double = False
    forbidden = False
    prev = ''
    for c in s:
        if prev + c in ['ab', 'cd', 'pq', 'xy']:
            forbidden = True
            break
        if c in 'aeiou':
            vowels += 1
        if c == prev:
            has_double = True
        prev = c
    if not forbidden and has_double and vowels >= 3:
        nice += 1

puzzle.answer_a = nice
print('Part1:', puzzle.answer_a)

nice = 0
for s in input_data.splitlines():
    two_pair = False
    repeat = False
    prev = dict()
    for i, c in enumerate(s.strip()):
        if c not in prev:
            prev[c] = set()
        prev[c].add(i)
        if (i-2) in prev[c]:
            repeat = True
        if i < len(s)-1:
            pair = s[i:i+2]
            if pair in prev:
                if i - prev[pair] > 1:
                    two_pair = True
            else:
                prev[pair] = i

        if two_pair and repeat:
            nice += 1
            break

puzzle.answer_b = nice
print('Part2:', puzzle.answer_b)
