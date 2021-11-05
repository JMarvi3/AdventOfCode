from aocd.models import Puzzle

dirs = [complex(0, 1), complex(1, 0), complex(0, -1), complex(-1, 0)]
instructions = Puzzle(2016, 1).input_data.split(', ')
pos = complex(0, 0)
curr_dir = 0

seen = set()
seen.add(pos)
part2 = None
for i in instructions:
    if i[0] == 'L':
        curr_dir = (curr_dir + 3) % 4
    else:
        curr_dir = (curr_dir + 1) % 4
    for _ in range(int(i[1:])):
        pos += dirs[curr_dir]
        if pos in seen and part2 is None:
            part2 = pos
        seen.add(pos)

print('part1:', int(abs(pos.real)+abs(pos.imag)))
print('part2:', int(abs(part2.real)+abs(part2.imag)))
