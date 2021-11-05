import re
from collections import Counter
from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

best_distance = 0
best_reindeer = ''
pat = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+)')

t = 2503
all_deer = []
for line in input_data.splitlines():
    deer, speed, fly, rest = pat.match(line).groups()
    all_deer.append((deer, int(speed), int(fly), int(fly) + int(rest)))

points = Counter()
for i in range(1, t + 1):
    best_distance = 0
    for deer, speed, fly, total in all_deer:
        full, rem = divmod(i, total)
        distance = fly * speed * full + speed * min(rem, fly)
        if distance > best_distance:
            best_distance = distance
            best_reindeer = deer
    points[best_reindeer] += 1

puzzle.answer_a = best_distance
print('Part1:', puzzle.answer_a, best_reindeer)

best_reindeer, best_distance = points.most_common(1)[0]
puzzle.answer_b = best_distance
print('Part2:', puzzle.answer_b, best_reindeer)
