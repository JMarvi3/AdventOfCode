from current_puzzle import current_puzzle
import aoc_lib

class DLNode:
    def __init__(self, value=None, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

    def remove(self):

        prev_node, next_node = self.prev, self.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def insert_before(self, node):
        self.insert_after(node.prev)

    def insert_after(self, node):
        self.prev, self.next = node, node.next
        self.prev.next = self.next.prev = self

    def __repr__(self):
        return f"{self.value}: ({self.next.value if self.next else None}, {self.prev.value if self.prev else None})"

    def rotate(self, n=0):
        curr = self
        assert n >= 0
        while n > 0:
            curr = curr.next
            n -= 1
        return curr


def all_nodes(head):
    curr = head
    nodes = []
    while True:
        nodes.append(curr)
        curr = curr.next
        if curr == head:
            break
    return nodes


def get_nodes(nums, key=1):
    nodes = []
    head = curr = DLNode()
    for num in nums:
        node = DLNode(num * key, prev_node=curr)
        nodes.append(node)
        curr.next = node
        curr = curr.next

    curr.next = head.next
    head.next.prev = curr
    return nodes


def do_mix(nodes):
    for node in nodes:
        if node.value != 0:
            curr = node.rotate(node.value % (len(nodes) - 1))
            node.remove()
            node.insert_after(curr)


def find_answer(nodes):
    zero = next(node for node in nodes if node.value == 0)
    return sum(zero.rotate(1000 * i).value for i in range(1, 4))


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('20.example').read()
# input_data = "[1, 2, -3, 3, -2, -2, 0, 4]"
# input_data = "1, 2, -3, 3, -2, 0, 8"

nums = aoc_lib.findall('{:d}', input_data)

nodes = get_nodes(nums)
do_mix(nodes)

puzzle.answer_a = find_answer(nodes)
print('Part1:', puzzle.answer_a)


KEY = 811589153
nodes = get_nodes(nums, KEY)

for _ in range(10):
    do_mix(nodes)

puzzle.answer_b = find_answer(nodes)
print('Part2:', puzzle.answer_b)
