from aocd.models import Puzzle


def swap(line, a, b):
    line = list(line)
    line[a], line[b] = line[b], line[a]
    return ''.join(line)


# moves = "s1,x3/4,pe/b".strip().split(",")
# n = 5

moves = Puzzle(2017, 16).input_data.strip().split(",")
n = 16


line = ''.join(chr(ord('a')+i) for i in range(n))
seen = {0: line}
time = 0
while True:
    for move in moves:
        if move[0] == 's':
            x = int(move[1:])
            line = line[-x:] + line[:-x]
        elif move[0] == 'x':
            line = swap(line, *map(int, move[1:].split("/")))
        elif move[0] == 'p':
            line = swap(line, *map(line.index, move[1:].split("/")))
    time += 1
    seen[time] = line
    if seen[time] == seen[0]:
        break

print('Part1:', seen[1])
print('Part2:', seen[1000000000 % time])
