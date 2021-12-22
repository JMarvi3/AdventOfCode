from current_puzzle import current_puzzle


class Literal:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)


class Node:
    def __init__(self, left, right, parent=None):
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"[{self.left},{self.right}]"

    def __int__(self):
        return 3*int(self.left) + 2*int(self.right)


def find_right(node):
    if not node.parent:
        return None
    temp = node
    while temp.parent and temp.parent.right == temp:
        temp = temp.parent
    if not temp.parent or temp.parent.right == temp:
        return None
    # node is in left tree of temp.parent
    temp = temp.parent.right
    while type(temp) == Node:
        temp = temp.left
    return temp


def find_left(node):
    if not node.parent:
        return None
    temp = node
    while temp.parent and temp.parent.left == temp:
        temp = temp.parent
    if not temp.parent or temp.parent.left == temp:
        return None
    # node is in right tree of temp.parent
    temp = temp.parent.left
    while type(temp) == Node:
        temp = temp.right
    return temp


def parse(s, pos=0):
    if s[pos] == '[':
        left, pos = parse(s, pos+1)
        assert s[pos] == ','
        right, pos = parse(s, pos+1)
        assert s[pos] == ']'
        new_node = Node(left, right)
        if type(left) == Node:
            left.parent = new_node
        if type(right) == Node:
            right.parent = new_node
        return new_node, pos+1
    else:
        return Literal(int(s[pos])), pos+1


def join(left, right):
    left.parent = right.parent = Node(left, right)
    return left.parent


def explode(node, depth=0):
    if type(node.left) != Node and type(node.right) != Node and depth >= 4:
        left, right = find_left(node), find_right(node)
        # print('explode', node, '->', left, right)
        if left:
            left.value += node.left.value
        if right:
            right.value += node.right.value
        if node.parent.left == node:
            node.parent.left = Literal(0, node.parent.left)
        else:
            node.parent.right = Literal(0, node.parent.right)
        return True
    elif type(node.left) == Node:
        if explode(node.left, depth+1):
            return True
    if type(node.right) == Node:
        return explode(node.right, depth+1)
    else:
        return False


def split(node):
    if type(node.left) != Node and node.left.value >= 10:
        # print('split', node.left)
        node.left = Node(Literal(node.left.value//2), Literal(node.left.value-node.left.value//2), node)
        return True
    if type(node.left) == Node and split(node.left):
        return True
    if type(node.right) != Node and node.right.value >= 10:
        # print('split', node.right)
        node.right = Node(Literal(node.right.value // 2), Literal(node.right.value - node.right.value // 2), node)
        return True
    if type(node.right) == Node:
        return split(node.right)
    else:
        return False


def reduce(node):
    if explode(node):
        return True
    return split(node)


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('18_2.example').read()
lines = []
for line in input_data.splitlines():
    root, _ = parse(line)
    lines.append(root)

root = lines[0]
for elem in lines[1:]:
    root = join(root, elem)
    while reduce(root):
        pass

# print(int(root))
puzzle.answer_a = int(root)
print('Part1:', puzzle.answer_a)

lines = input_data.splitlines()
best_mag = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i != j:
            root = join(parse(lines[i])[0], parse(lines[j])[0])
            while reduce(root): pass
            best_mag = max(best_mag, int(root))
# print(best_mag)
puzzle.answer_b = best_mag
print('Part2:', puzzle.answer_b)
