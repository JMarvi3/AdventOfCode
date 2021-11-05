import time
import hashlib
from current_puzzle import current_puzzle

start = time.perf_counter()
puzzle = current_puzzle()

part1 = None
i = 1
secret = puzzle.input_data
while True:
    m = hashlib.md5()
    m.update(bytes(secret + str(i), 'utf-8'))
    digest = m.hexdigest()
    if digest[:5] == '00000':
        if part1 is None:
            part1 = i
        if digest[5] == '0':
            break
    i += 1

print(f"time: {time.perf_counter()-start:.2f}s")

puzzle.answer_a = part1
print('Part1:', puzzle.answer_a)
puzzle.answer_b = i
print('Part2:', puzzle.answer_b)
