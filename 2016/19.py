from aocd.models import Puzzle


class Node:
    next = None
    prev = None
    val = 0
    count = 1

    def __init__(self, val):
        self.val = val


def final_elf(num, opposite=False):
    n = num
    root = curr_elf = Node(1)
    for i in range(2, n + 1):
        new_elf = Node(i)
        new_elf.prev = curr_elf
        curr_elf.next = new_elf
        curr_elf = new_elf
    curr_elf.next = root
    root.prev = curr_elf

    if opposite:
        opp_elf = root
        for i in range(n // 2):
            opp_elf = opp_elf.next

    curr_elf = root

    while curr_elf.next != curr_elf:
        if opposite:
            curr_elf.count += opp_elf.count
            opp_elf.prev.index = opp_elf.next
            opp_elf.next.prev = opp_elf.prev
            # print(curr_elf.val, opp_elf.val)
            opp_elf = opp_elf.next
            n -= 1
            if n % 2 == 0:
                opp_elf = opp_elf.index
        else:
            curr_elf.count += curr_elf.next.count
            curr_elf.next = curr_elf.next.next
        curr_elf = curr_elf.next

    assert curr_elf.count == num
    return curr_elf.val


n = int(Puzzle(2016, 19).input_data)
print('part1:', final_elf(n))
print('part2:', final_elf(n, opposite=True))
