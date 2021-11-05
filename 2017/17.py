from aocd.models import Puzzle


class Node:
    def __init__(self, val, next_node=None):
        self.next = next_node
        self.val = val


steps = int(Puzzle(2017, 17).input_data)
# steps = 3

ptr = Node(0)
ptr.next = ptr
for i in range(1, 2018):
    for _ in range(steps):
        ptr = ptr.next
    ptr.next = Node(i, ptr.next)
    ptr = ptr.next
print('Part1:', ptr.next.val)

pos = second = 0
length = 1
for i in range(1, 50_000_000):
    pos = (pos+steps) % length
    if pos == 0:
        second = i
    length += 1
    pos += 1
print('Part1:', second)
