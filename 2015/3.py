from current_puzzle import current_puzzle


def get_houses(houses, moves):
    pos = [0, 0]
    houses.add(tuple(pos))
    for c in moves:
        if c == '^':
            pos[1] += 1
        elif c == 'v':
            pos[1] -= 1
        elif c == '<':
            pos[0] -= 1
        elif c == '>':
            pos[0] += 1
        houses.add(tuple(pos))
    return houses


puzzle = current_puzzle()
input_data = puzzle.input_data

houses = get_houses(set(), input_data)
puzzle.answer_a = len(houses)
print('Part1:', puzzle.answer_a)

houses = get_houses(set(), input_data[::2])
houses = get_houses(houses, input_data[1::2])
puzzle.answer_b = len(houses)
print('Part2:', puzzle.answer_b)
