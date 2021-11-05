from current_puzzle import current_puzzle


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def __str__(self):
        return f"Node: {len(self.children)}, {len(self.metadata)} ({sum(self.metadata)})"

    def metadata_sum(self):
        return sum(self.metadata) + sum(map(Node.metadata_sum, self.children))

    def value(self):
        if not self.children:
            return sum(self.metadata)
        else:
            return sum(self.children[entry-1].value() for entry in self.metadata if 0 < entry <= len(self.children))


def get_node(data, pos=0, depth=0):
    data = list(data)
    num_children, num_meta = data[pos:pos + 2]
    pos += 2
    children = []
    for _ in range(num_children):
        child, pos = get_node(data, pos, depth + 1)
        children.append(child)
    metadata = data[pos:pos + num_meta]
    pos += num_meta
    node = Node(children, metadata)
    if depth == 0:
        assert pos == len(data)
        return node
    else:
        return node, pos


puzzle = current_puzzle()
input_data = puzzle.input_data
root = get_node(map(int, input_data.split()))

puzzle.answer_a = root.metadata_sum()
print('Part1:', puzzle.answer_a)

puzzle.answer_b = root.value()
print('Part2:', puzzle.answer_b)
