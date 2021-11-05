from aocd.models import Puzzle
from collections import deque

areas = dict()
scanners = dict()


def update_scanners(scanners, areas):
    for depth, scanner in scanners.items():
        scanner[0] += scanner[1]
        if scanner[0] == 0 or scanner[0] == areas[depth] - 1:
            scanner[1] *= -1


lines = Puzzle(2017, 13).input_data.splitlines()
#lines = ["0: 3", "1: 2", "4: 4", "6: 4"]
for line in lines:
    d, r = map(int, line.split(': '))
    areas[d] = r

max_depth = max(areas.keys())
scanners = {d: [0, 1] for d in areas}
severity = 0
for pos in range(max_depth + 1):
    if pos in scanners and scanners[pos][0] == 0:
        severity += pos * areas[pos]
    update_scanners(scanners, areas)

print(severity)

scanners = {d: [0, 1] for d in areas}
packets = []
delay = 0
while True:
    packets.append([0, delay])
    packets = [[packet[0]+1, packet[1]] for packet in packets if not (packet[0] in scanners and scanners[packet[0]][0] == 0)]
    if packets and packets[0][0] > max_depth:
        print(packets[0][1])
        break
    update_scanners(scanners, areas)
    delay += 1
