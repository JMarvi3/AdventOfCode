from aocd.models import Puzzle

puzzle = Puzzle(2018, 6)
points = [tuple(map(int, line.split(','))) for line in puzzle.input_data.splitlines()]
x, y = zip(*points)
min_x, max_x = min(x), max(x)
min_y, max_y = min(y), max(y)

areas = [0] * len(points)
finite_pts = set(range(len(points)))
close_area = 0

for x in range(min_x-1, max_x+2):
    for y in range(min_y-1, max_y+2):
        total = 0
        closest, closest_dist = None, float('inf')
        for i in range(len(points)):
            dist = abs(points[i][0]-x) + abs(points[i][1]-y)
            total += dist
            if dist <= closest_dist and closest:
                areas[closest] -= 1
                closest = None
            if dist < closest_dist:
                closest_dist = dist
                closest = i
                areas[i] += 1
        if total < 10_000:
            close_area += 1
        if (x in [min_x-1, max_x+1] or y in [min_y-1, max_y+1]) and closest in finite_pts:
            # if a border point is closest to one of the points, all the points outside will be closest
            finite_pts.remove(closest)

        #print('*' if total < 10_000 else '.', end='')
        #print('*' if (x, y) in points else chr(closest+ord('0')) if closest else '.', end='')
    #print()

max_pt = max(finite_pts, key=lambda pt: areas[pt])
puzzle.answer_a = areas[max_pt]
print('Part1:', areas[max_pt])
print('Part2:', close_area)
print(puzzle.answers)
