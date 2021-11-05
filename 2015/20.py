from current_puzzle import current_puzzle
import time

puzzle = current_puzzle()
p = int(puzzle.input_data)

start = time.perf_counter()

max_house = p//10

houses = [0]*max_house
for elf in range(1, max_house):
    inc = elf * 10
    for house in range(elf, max_house, elf):
        houses[house] += inc
    if houses[elf] >= p:
        break

puzzle.answer_a = elf
print('Part1:', puzzle.answer_a)

part1 = time.perf_counter()

houses = [0]*max_house
for elf in range(1, max_house):
    inc = elf * 11
    for house in range(elf, min(51 * elf, max_house), elf):
        houses[house] += inc
    if houses[elf] >= p:
        break

puzzle.answer_b = elf
print('Part2:', puzzle.answer_b)

end = time.perf_counter()
print(f"time: {end-start:.3f}s total, {part1-start:.3f}s/{end-part1:.3f}s")
