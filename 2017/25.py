checksum = 12656374
rules = {'A': ((1, 1, 'B'), (0, -1, 'C')), 'B': ((1, -1, 'A'), (1, -1, 'D')), 'C': ((1, 1, 'D'), (0, 1, 'C')),
         'D': ((0, -1, 'B'), (0, 1, 'E')), 'E': ((1, 1, 'C'), (1, -1, 'F')), 'F': ((1, -1, 'E'), (1, 1, 'A'))}

tape = dict()
pos, state = 0, 'A'
for _ in range(checksum):
    tape[pos], move, state = rules[state][tape.get(pos, 0)]
    pos += move

print(sum(tape.values()))
