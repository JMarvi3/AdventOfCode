from aocd.models import Puzzle

s = Puzzle(2017, 1).input_data
part1 = sum(int(s[i]) * (s[i] == s[(i + 1) % len(s)]) for i in range(len(s)))
print(part1)

part2 = sum(int(s[i]) * (s[i] == s[(i + len(s)//2) % len(s)]) for i in range(len(s)))
print(part2)
