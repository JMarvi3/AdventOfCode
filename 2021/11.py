from current_puzzle import current_puzzle


def print_octopi(octopi):
    max_x = max(int(pt.real) for pt in octopi)
    max_y = max(int(pt.imag) for pt in octopi)
    for y in range(max_y + 1):
        print(', '.join([str(octopi[x + y * 1j]) for x in range(max_x + 1)]))
    print()


def update_octopi(octopi):
    flashed = set()
    for pt in octopi:
        octopi[pt] += 1
    while new_flashes := list(pt for pt, val in octopi.items() if pt not in flashed and val > 9):
        flashed.update(new_flashes)
        for pt in new_flashes:
            for d in dirs:
                if pt+d in octopi and pt+d not in flashed:
                    octopi[pt+d] += 1
    for pt in flashed:
        octopi[pt] = 0
    return len(flashed)


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('11.example').read()
dirs = {x + y * 1j for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}

octopi = {x + y * 1j: int(c) for y, row in enumerate(input_data.splitlines()) for x, c in enumerate(row)}
part2_octopi = octopi.copy()
puzzle.answer_a = sum(update_octopi(octopi) for _ in range(100))
print('Part1:', puzzle.answer_a)

octopi = part2_octopi
step = 1
while update_octopi(octopi) != len(octopi):
    step += 1
puzzle.answer_b = step
print('Part2:', puzzle.answer_b)
