from collections import deque, defaultdict
from heapq import heappop, heappush, heapify
from current_puzzle import current_puzzle
import time


def move_storms(storms):
    new_storms = set()
    for x, y, d in storms:
        if d == '<':
            x = x - 1 if x > 1 else max_x - 1
        elif d == '>':
            x = 1 if x == max_x - 1 else x + 1
        elif d == '^':
            y = y - 1 if y > 1 else max_y - 1
        elif d == 'v':
            y = 1 if y == max_y - 1 else y + 1
        else:
            print('error', x, y, d)
            exit(1)
        new_storms.add((x, y, d))
    return new_storms


def dist(a, b): return (b[0]-a[0])+(b[1]-a[1])


def astar(start, goal, start_time=0):
    global storms, all_storms, max_t
    scores = defaultdict(lambda: float('inf'))
    heap = [[dist(start, goal)+start_time, start_time, start]]
    while heap:
        _, t, (x, y) = heappop(heap)
        if (x, y) == goal:
            return t
        for dt in range(max_t + 1, t + 1 + 1):
            storms = move_storms(storms)
            all_storms.update(((x, y, dt) for x, y, _ in storms))
            max_t = dt
        for d in dirs:
            new_x, new_y = x + d[0], y + d[1]

            if (new_x, new_y) not in walls and (new_x, new_y, t+1) not in all_storms:
                # print(new_x, new_y, t + 1)
                h = dist((new_x, new_y), goal) + t + 1
                for entry in heap:
                    if entry[2] == (new_x, new_y):
                        if h < entry[0]:
                            entry[0] = h
                            entry[1] = t + 1
                            heapify(heap)
                        break
                else:
                    heappush(heap, [dist((new_x, new_y), goal)+t+1, t+1, (new_x, new_y)])


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('24.example').read()

walls = set()
storms = set()
goal_x = goal_y = None
for y, row in enumerate(input_data.splitlines()):
    for x, c in enumerate(row):
        if c == '#':
            walls.add((x, y))
        elif c == '.':
            goal_x, goal_y = x, y
        else:
            storms.add((x, y, c))
max_x, max_y = x, y

walls.update([(1, -1), (goal_x, goal_y+1)])

all_storms = {(x, y, 0) for x, y, _ in storms}
max_t = 0

start = (1, 0)
goal = (goal_x, goal_y)
part1 = astar(start, goal)

puzzle.answer_a = part1
print('Part1:', puzzle.answer_a)

part2 = astar(goal, start, part1+1)
part2 = astar(start, goal, part2+1)

puzzle.answer_b = part2
print('Part2:', puzzle.answer_b)
