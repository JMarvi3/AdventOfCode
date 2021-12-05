from current_puzzle import current_puzzle
from collections import Counter
import re

puzzle = current_puzzle()
input_data = puzzle.input_data


def find_duplicates(lines, part2=False):
    points = Counter()
    for (x0, y0), (x1, y1) in lines:
        if x0 == x1:
            points.update((x0, i) for i in range(y0, y1+1))
        elif y0 == y1:
            points.update((i, y0) for i in range(x0, x1 + 1))
        elif part2:
            if y0 < y1:
                points.update((x0 + i, y0 + i) for i in range(y1 - y0 + 1))
            else:
                points.update((x0 + i, y0 - i) for i in range(y0 - y1 + 1))
    return sum(points[pt] > 1 for pt in points)


# import time
# start = time.perf_counter_ns()

pat = re.compile(r"\d+")
lines = []
for line in input_data.splitlines():
    x0, y0, x1, y1 = map(int, pat.findall(line))
    lines.append(sorted([(x0, y0), (x1, y1)]))

# parse_time = (time.perf_counter_ns()-start)/1000000
# start = time.perf_counter_ns()

puzzle.answer_a = find_duplicates(lines)
# part1_time = (time.perf_counter_ns()-start)/1000000
print('Part1:', puzzle.answer_a)

# start = time.perf_counter_ns()
puzzle.answer_b = find_duplicates(lines, part2=True)
# part2_time = (time.perf_counter_ns()-start)/1000000
print('Part2:', puzzle.answer_b)

# print(f"Time elapsed (parse/part1/part2): {parse_time:.3f}ms/{part1_time:.3f}ms/{part2_time:.3f}ms")
