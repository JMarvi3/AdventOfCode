from current_puzzle import current_puzzle
from collections import defaultdict


def add_pt(pt1, pt2): return pt1[0] + pt2[0], pt1[1] + pt2[1]


def neighbors(elf):
    return ((x + elf[0], y + elf[1]) for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0,0))


def do_round(elves, round):
    # elves.sort()
    new_elves = []
    count = defaultdict(int)
    num_moves = 0
    for elf in elves:
        neighbor_count = sum(neighbor in elves for neighbor in neighbors(elf))
        if neighbor_count == 0:
            # print(f"{elf} doesn't move")
            new_elves.append(elf)
            count[elf] += 1
        else:
            for i in range(4):
                move, tests = moves[(i+round)%4]
                if all(add_pt(elf, test) not in elves for test in tests):
                    new_elf = add_pt(elf, move)
                    num_moves += 1
                    new_elves.append(new_elf)
                    count[new_elf] += 1
                    # print(f"{elf} proposes move to {new_elf}")
                    break
            else:
                # print(f"{elf} can't move")
                new_elves.append(elf)
                count[elf] += 1
    assert len(new_elves) == len(elves)
    # print(count, new_elves)
    return [new_elf if count[new_elf] == 1 else elves[i] for i, new_elf in enumerate(new_elves)], num_moves


def get_bounds(elves):
    return min(elf[0] for elf in elves), max(elf[0] for elf in elves), min(elf[1] for elf in elves), max(
        elf[1] for elf in elves)


def draw_elves(elves):
    min_x, max_x, min_y, max_y = get_bounds(elves)
    print((min_x, min_y))
    for y in range(min_y, max_y + 1):
        print(''.join('#' if (x, y) in elves else '.' for x in range(min_x, max_x + 1)))


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('23.example').read()

moves = [((0, -1), ((-1, -1), (0, -1), (1, -1))), ((0, 1), ((-1, 1), (0, 1), (1, 1))),
         ((-1, 0), ((-1, -1), (-1, 0), (-1, 1))), ((1, 0), ((1, -1), (1, 0), (1, 1)))]

elves = []
for y, row in enumerate(input_data.splitlines()):
    for x, c in enumerate(row):
        if c == '#':
            elves.append((x, y))

# draw_elves(elves)
for i in range(10):
    elves, num_moves = do_round(elves, i)
    # print(i+1, num_moves, len(elves))
    # draw_elves(elves)

min_x, max_x, min_y, max_y = get_bounds(elves)
puzzle.answer_a = (max_x-min_x+1)*(max_y-min_y+1) - len(elves)
print('Part1:', puzzle.answer_a)

for i in range(10, 10000):
    elves, num_moves = do_round(elves, i)
    # print(i+1, num_moves, len(elves))
    if num_moves == 0:
        break

puzzle.answer_b = i+1
print('Part2:', puzzle.answer_b)
