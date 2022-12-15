import parse
from current_puzzle import current_puzzle


def merge_intervals(intervals):
    intervals.sort()
    merged = []
    curr = intervals[0]
    for interval in intervals:
        if interval[0] <= curr[1]:
            curr[1] = max(curr[1], interval[1])
        else:
            merged.append(curr)
            curr = interval
    merged.append(curr)
    return merged


def get_count(intervals):
    count = 0
    for interval in intervals:
        count += interval[1] - interval[0]
    return count


def make_merged(sensors, y):
    intervals = []
    for (sx, sy), distance in sensors:
        if abs(y - sy) <= distance:
            delta = distance - abs(sy - y)
            intervals.append([sx - delta, sx + delta])
    return merge_intervals(intervals)


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('15.example').read()

pat = parse.compile("Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}")
sensors = []
min_x = min_y = float('inf')
max_x = max_y = -float('inf')
max_distance = -float('inf')
min_distance = float('inf')
for line in input_data.splitlines():
    sx, sy, bx, by = pat.parse(line).fixed
    distance = dist((sx, sy), (bx, by))
    sensors.append(((sx, sy), distance))

puzzle.answer_a = get_count(make_merged(sensors, 2000000))
print('Part1:', puzzle.answer_a)

MAX = 4000000
all_possibilities = ((y, make_merged(sensors, y)) for y in range(0, MAX+1))
gap_y, (range1, range2) = next((y, merged) for y, merged in all_possibilities if len(merged) != 1)
assert range2[0] - range1[1] == 2
gap_x = range1[1] + 1

puzzle.answer_b = gap_x * MAX + gap_y
print('Part2:', puzzle.answer_b)
