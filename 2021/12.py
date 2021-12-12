from current_puzzle import current_puzzle
import networkx


def dfs(g, end, path):
    count = 0
    if path[-1] == end:
        count += 1
    for neighbor in g[path[-1]]:
        if neighbor != neighbor.lower() or neighbor not in path:
            count += dfs(g, end, path + [neighbor])
    return count


def dfs_part2(g, end, path: list, revisited=False):
    if path[-1] == end:
        return 1
    count = 0
    for neighbor in g[path[-1]]:
        if neighbor != neighbor.lower() or neighbor not in path:
            count += dfs_part2(g, end, path + [neighbor], revisited)
        elif neighbor != 'start' and not revisited:
            count += dfs_part2(g, end, path + [neighbor], True)
    return count


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('12_3.example').read()

g = networkx.Graph()
for line in input_data.splitlines():
    g.add_edge(*line.split('-'))

puzzle.answer_a = dfs(g, 'end', ['start'])
print('Part1:', puzzle.answer_a)

puzzle.answer_b = dfs_part2(g, 'end', ['start'])
print('Part2:', puzzle.answer_b)
