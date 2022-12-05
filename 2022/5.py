from current_puzzle import current_puzzle
from collections import deque, defaultdict
from copy import deepcopy
import aoc_lib

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

stack_input, moves = map(str.splitlines, input_data.split('\n\n'))
clean_stacks = defaultdict(deque)
for line in stack_input[:-1]:
    for i, c in enumerate(line[1::4]):
        if c != ' ':
            clean_stacks[i+1].append(c)
max_stack = max(clean_stacks.keys())

stacks = deepcopy(clean_stacks)
for move in moves:
    i, f, t = aoc_lib.findall('{:d}', move)
    for _ in range(i):
        stacks[t].appendleft(stacks[f].popleft())
part1_answer = ''.join(stacks[i][0] for i in range(i, max_stack+1))

puzzle.answer_a = part1_answer
print('Part1:', puzzle.answer_a)

stacks = deepcopy(clean_stacks)
for move in moves:
    i, f, t = aoc_lib.findall('{:d}', move)
    new_stack = deque()
    for _ in range(i):
        new_stack.appendleft(stacks[f].popleft())
    while new_stack:
        stacks[t].appendleft(new_stack.popleft())

part2_answer = ''.join(stacks[i][0] for i in range(i, max_stack+1))

puzzle.answer_b = part2_answer
print('Part2:', puzzle.answer_b)
