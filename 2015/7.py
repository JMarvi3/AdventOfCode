from current_puzzle import current_puzzle


def eval_wire(wire):
    global memo
    global circuit
    if wire in memo:
        return memo[wire]
    if wire not in circuit:
        answer = int(wire)
    else:
        rule = circuit[wire]
        if len(rule) == 1:
            answer = eval_wire(rule[0])
        elif len(rule) == 2:
            answer = 65535 ^ eval_wire(rule[1])
        elif rule[1] == 'AND':
            answer = eval_wire(rule[0]) & eval_wire(rule[2])
        elif rule[1] == 'OR':
            answer = eval_wire(rule[0]) | eval_wire(rule[2])
        elif rule[1] == 'LSHIFT':
            answer = eval_wire(rule[0]) << eval_wire(rule[2])
        elif rule[1] == 'RSHIFT':
            answer = eval_wire(rule[0]) >> eval_wire(rule[2])
        else:
            print('error', wire, rule)
    memo[wire] = answer
    return answer


puzzle = current_puzzle()
input_data = puzzle.input_data

circuit = dict()
for line in input_data.splitlines():
    rule, wire = line.split(' -> ')
    circuit[wire] = rule.split()

memo = dict()
puzzle.answer_a = eval_wire('a')
print('part1:', puzzle.answer_a)

circuit['b'] = [str(puzzle.answer_a)]
memo = dict()
puzzle.answer_b = eval_wire('a')
print('Part2:', puzzle.answer_b)
