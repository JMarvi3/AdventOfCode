from aocd.models import Puzzle
from time import perf_counter

#input_data = "Generator A starts with 65\nGenerator B starts with 8921"
input_data = Puzzle(2017, 15).input_data

start = perf_counter()

gens = [int(line.split("with ")[1]) for line in input_data.splitlines()]
factor = [16807, 48271]

matches = 0
for _ in range(40_000_000):
    gens[0] = gens[0] * factor[0] % 2147483647
    gens[1] = gens[1] * factor[1] % 2147483647
    if (gens[0] ^ gens[1]) & 0xffff == 0:
        matches += 1

part1_time = perf_counter()
print(f"Part1: {matches} took {part1_time - start:0.04}s")

gens = [int(line.split("with ")[1]) for line in input_data.splitlines()]
matches = 0
calcs = 0
for _ in range(5_000_000):
    while True:
        gens[0] = gens[0] * factor[0] % 2147483647
        calcs += 1
        if gens[0] % 4 == 0:
            break
    while True:
        gens[1] = gens[1] * factor[1] % 2147483647
        calcs += 1
        if gens[1] % 8 == 0:
            break
    if (gens[0] ^ gens[1]) & 0xffff == 0:
        matches += 1

print(f"Part2: {matches} took {perf_counter() - part1_time:0.04}s ({calcs} calcs)")
