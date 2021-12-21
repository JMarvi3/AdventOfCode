from current_puzzle import current_puzzle
import networkx


def solve(risks, dest):
    g = networkx.DiGraph()
    g.add_weighted_edges_from(
        [(pt, pt + d, risks[pt + d]) for d in [1, 1j, -1, -1j] for pt in risks if pt + d in risks])
    return networkx.dijkstra_path_length(g, 0, dest)


def increment_with_wrap(n):
    return 1 if n == 9 else n + 1


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('15.example').read()

risks = dict()
x = y = 0
for y, row in enumerate(input_data.splitlines()):
    for x, c in enumerate(row):
        risks[x + y * 1j] = int(c)

puzzle.answer_a = solve(risks, x + y * 1j)
print('Part1:', puzzle.answer_a)

size = x + 1
assert x == y

for y in range(size):
    for x in range(size, size * 5):
        risks[x + y * 1j] = increment_with_wrap(risks[(x - size) + y * 1j])

for y in range(size, size * 5):
    for x in range(size * 5):
        risks[x + y * 1j] = increment_with_wrap(risks[x + (y - size) * 1j])

puzzle.answer_b = solve(risks, x + y * 1j)
print('Part2:', puzzle.answer_b)

# for y in range(size*5):
#     print(''.join(map(str, (risks[x+y*1j] for x in range(size*5)))))
