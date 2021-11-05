import time
from current_puzzle import current_puzzle


def look_and_say(s):
    result = ''
    count = 1
    prev = s[0]
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            result += str(count) + prev
            count = 1
            prev = c
    result += str(count) + prev
    return result


puzzle = current_puzzle()
input_data = puzzle.input_data

start = time.perf_counter()

s = input_data.strip()
for _ in range(40):
    s = look_and_say(s)

puzzle.answer_a = len(s)
print('Part1:', puzzle.answer_a)

part1 = time.perf_counter()

for _ in range(10):
    s = look_and_say(s)

puzzle.answer_b = len(s)
print('Part2:', puzzle.answer_b)

print(f"time: {part1-start:.2f}s / {time.perf_counter()-part1:.2f}s")
