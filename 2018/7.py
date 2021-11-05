import copy
import heapq
import re
from collections import defaultdict
from current_puzzle import current_puzzle


def parse_data(lines):
    pat = re.compile(r" ([A-Z]) ")
    requires = defaultdict(set)
    provides = defaultdict(set)
    steps = set()
    for line in map(pat.findall, lines):
        steps.update(line)
        provides[line[0]].add(line[1])
        requires[line[1]].add(line[0])
    start_steps = set(provides) - set(requires)
    return len(steps), requires, provides, start_steps


def build_sleigh(num_steps, requires, provides, start_steps, num_workers=1, offset=60):
    requires = copy.deepcopy(requires)
    heap = list(start_steps)
    heapq.heapify(heap)
    workers = []
    time, path = 0, ''
    while len(path) < num_steps:
        while workers and workers[0][0] == time:
            _, step = heapq.heappop(workers)
            path += step
            for provided in provides[step]:
                requires[provided].discard(step)
                if not requires[provided]:
                    heapq.heappush(heap, provided)
        while heap and len(workers) < num_workers:
            step = heapq.heappop(heap)
            delay = offset + 1 + ord(step) - ord('A')
            heapq.heappush(workers, (time + delay, step))
        if workers:
            time = workers[0][0]
    return time, path


if True:  # example
    data = parse_data(open('7.example').readlines())
    _, path = build_sleigh(*data)
    seconds, _ = build_sleigh(*data, num_workers=2, offset=0)
    print('Example:', path, seconds)

puzzle = current_puzzle()
data = parse_data(puzzle.input_data.splitlines())

_, path = build_sleigh(*data)
puzzle.answer_a = path
print('Part1:', puzzle.answer_a)

seconds, _ = build_sleigh(*data, num_workers=5)
puzzle.answer_b = seconds
print('Part2:', puzzle.answer_b)
