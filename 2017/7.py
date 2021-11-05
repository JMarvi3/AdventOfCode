from aocd.models import Puzzle
from collections import Counter

programs = set()
children = dict()
parent = dict()
weight = dict()

for line in Puzzle(2017, 7).input_data.splitlines():
    line = line.strip().split(" -> ")
    program = line[0].split()[0]
    weight[program] = int(line[0].split()[1][1:-1])
    programs.add(program)
    if len(line) > 1:
        children[program] = line[1].split(", ")
        for child in children[program]:
            parent[child] = program
root = (programs - set(parent)).pop()

print('Part1:', root)


def calc_weight(node):
    if node in children:
        weight[node] += sum(calc_weight(child) for child in children[node])
    return weight[node]


def find_wrong(node):
    if node in children:
        weights = [weight[child] for child in children[node]]
        if max(weights) != min(weights):
            global wrong
            wrong = node
            for child in children[node]:
                find_wrong(child)


calc_weight(root)
wrong = ""
find_wrong(root)
wrong_children = children[wrong]
counter = Counter(weight[child] for child in wrong_children)
right_weight = max(counter, key=counter.get)
wrong = [child for child in wrong_children if weight[child] != right_weight][0]
print('Part2:', right_weight - sum(weight[child] for child in children[wrong]))
