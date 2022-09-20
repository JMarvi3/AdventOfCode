from current_puzzle import current_puzzle
from rots import apply_int_rot
from time import perf_counter
import parse

puzzle = current_puzzle()
input_data = puzzle.input_data


def dist(point1, point2):
    return frozenset(abs(a - b) for a, b in zip(point1, point2))


def diff(point1, point2):
    return point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]


def find_common_pts(points1, points2, rot):
    points2_diffs = {diff(apply_int_rot(points2[i], rot), apply_int_rot(points2[j], rot)): i
                     for i in range(len(points2)) for j in range(i+1, len(points2))}
    points1_diffs = {diff(points1[i], points1[j]): i
                     for i in range(len(points1)) for j in range(i+1, len(points1))}
    return [(points1_diffs[d], points2_diffs[d]) for d in points2_diffs if d in points1_diffs]


def find_common_dists(point1, point2):
    point2_dists = {dist(point2[i], point2[j])
                    for i in range(len(point2)) for j in range(i+1, len(point2))}
    point1_dists = {dist(point1[i], point1[j])
                    for i in range(len(point1)) for j in range(i+1, len(point1))}
    return len(point1_dists.intersection(point2_dists))


start = perf_counter()
# data = open('19.example').read()
data = input_data
reports = []
for report in data.split('\n\n'):
    lines = report.splitlines()[1:]
    reports.append(list(tuple(parse.parse("{:d},{:d},{:d}", line)) for line in lines))

print('Number of scanners:', len(reports))
print('Starting count:', sum(len(report) for report in reports))
scanner_pos = [(0, 0, 0)]

all_scanners = set(range(1, len(reports)))
while all_scanners:
    found_scanner = []
    for scanner in all_scanners:
        if find_common_dists(reports[0], reports[scanner]) >= 12:
            for rot in range(24):
                common = find_common_pts(reports[0], reports[scanner], rot)
                if len(common) >= 12:
                    found_scanner.append(scanner)
                    left_pt_idx, right_pt_idx = common[0]
                    left_pt, right_pt = reports[0][left_pt_idx], apply_int_rot(reports[scanner][right_pt_idx], rot)
                    translate = diff(right_pt, left_pt)
                    scanner_pos.append(diff(left_pt, right_pt))
                    reports[0] = list(set(reports[0])
                                      | set(diff(apply_int_rot(pt, rot), translate) for pt in reports[scanner]))
                    break
    all_scanners.difference_update(found_scanner)
    # print(found_scanner)
print('Final count:', len(reports[0]))
puzzle.answer_a = len(reports[0])

max_dist = 0
for i in range(len(scanner_pos)):
    for j in range(i + 1, len(scanner_pos)):
        max_dist = max(max_dist, sum(dist(scanner_pos[i], scanner_pos[j])))
print('Max distance:', max_dist)
puzzle.answer_b = max_dist
print(f'done in {perf_counter() - start:.3f}s')
