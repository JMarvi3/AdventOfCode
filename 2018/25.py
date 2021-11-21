from current_puzzle import current_puzzle
import re
import time


def distance(star1, star2):
    return sum(abs(star1[i]-star2[i]) for i in range(4))


def get_constellation(stars: set):
    stack = [stars.pop()]
    while stack:
        star = stack.pop()
        new_stars = set(other_star for other_star in stars if distance(star, other_star) <= 3)
        stack.extend(new_stars)
        stars -= new_stars


puzzle = current_puzzle()
input_data = puzzle.input_data

stars = set(tuple(map(int, re.findall(r"-?\d+", line))) for line in input_data.splitlines())

start = time.perf_counter_ns()

count = 0
while stars:
    count += 1
    get_constellation(stars)

puzzle.answer_a = count
print('Part1:', puzzle.answer_a)

print(f"Elapsed time: {(time.perf_counter_ns()-start)/1_000_000:.2f}ms")
