from current_puzzle import current_puzzle
from functools import reduce
from operator import mul


class Literal:
    def __init__(self, version, value):
        self.version = version
        self.value = value

    def ver_sum(self):
        return self.version


class Operator:
    def __init__(self, version, op_type, children):
        self.version = version
        self.type = op_type
        self.children = children

    def ver_sum(self):
        return sum(child.ver_sum() for child in self.children) + self.version

    @property
    def value(self):
        values = [child.value for child in self.children]
        if self.type == 0:
            return sum(values)
        elif self.type == 1:
            return reduce(mul, values)
        elif self.type == 2:
            return min(values)
        elif self.type == 3:
            return max(values)
        elif self.type == 5:
            return values[0] > values[1]
        elif self.type == 6:
            return values[0] < values[1]
        elif self.type == 7:
            return values[0] == values[1]
        else:
            assert False, 'Error'


def parse(s, pos=0):
    version = int(s[pos:pos+3], 2)
    op_type = int(s[pos+3:pos+6], 2)
    pos += 6
    if op_type == 4:
        value = 0
        while s[pos] == '1':
            value = value * 16 + int(s[pos+1:pos+5], 2)
            pos += 5
        value = value * 16 + int(s[pos + 1:pos + 5], 2)
        return pos+5, Literal(version, value)
    else:
        children = []
        if s[pos] == '1':
            size = int(s[pos + 1: pos + 12], 2)
            pos += 12
            for _ in range(size):
                pos, child = parse(s, pos)
                children.append(child)
            return pos, Operator(version, op_type, children)
        else:
            end_pos = int(s[pos + 1: pos + 16], 2) + pos + 16
            pos += 16
            while pos < end_pos:
                pos, child = parse(s, pos)
                children.append(child)
            return pos, Operator(version, op_type, children)


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

s = f"{int(input_data, 16):b}"
_, root = parse(s)

puzzle.answer_a = root.ver_sum()
print('Part1:', puzzle.answer_a)

puzzle.answer_b = root.value
print('Part2:', puzzle.answer_b)
