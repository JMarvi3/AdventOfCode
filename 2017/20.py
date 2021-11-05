from aocd.models import Puzzle
import parse


def update(a, b):
    no_further_updates_needed = True
    for i in range(len(a)):
        for axis in range(3):
            if b[i][axis] != 0 and ((a[i][axis] < 0 and b[i][axis] > 0) or (a[i][axis] > 0 and b[i][axis] < 0)):
                no_further_updates_needed = False
            a[i][axis] += b[i][axis]
    return no_further_updates_needed


pat = parse.compile("p=<{:d},{:d},{:d}>, v=<{:d},{:d},{:d}>, a=<{:d},{:d},{:d}>")

sample = "p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>\np=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>\n" + \
        "p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>\np=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>"
pos, vel, acc = [], [], []
for line in Puzzle(2017, 20).input_data.splitlines():
    r = pat.parse(line.strip())
    pos.append(list(r[:3]))
    vel.append(list(r[3:6]))
    acc.append(r[6:])

indexes = set(range(len(pos)))
while True:
    done_vel = update(vel, acc)
    done_pos = update(pos, vel)
    if done_vel and done_pos:
        break
    seen = dict()
    remove = set()
    for index in indexes:
        t = tuple(pos[index])
        if t in seen:
            remove.update([seen[t], index])
        seen[t] = index
    indexes -= remove

min_pos = min(pos, key=lambda p: sum(map(abs, p)))
print('Part1:', pos.index(min_pos))
print('Part2:', len(indexes))
