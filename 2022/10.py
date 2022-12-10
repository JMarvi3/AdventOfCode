from current_puzzle import current_puzzle
import aoc_lib


def calc_strength(cycle, x):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return cycle * x
    else:
        return 0


def paint(board, cycle, x):
    row, col = (cycle-1)//40, (cycle-1)%40
    if row == len(board):
        board.append([' ']*40)
    board[row][col] = '*' if col in [x - 1, x, x + 1] else ' '


puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('10.example').read()
lines = input_data.splitlines()
x = 1
strength = pc = 0
cycle = 1
board = []
for instr in lines:
    paint(board, cycle, x)
    cycle += 1
    strength += calc_strength(cycle, x)
    paint(board, cycle, x)
    if instr[0] == 'a':
        cycle += 1
        x += int(instr.split(' ')[1])
        strength += calc_strength(cycle, x)

puzzle.answer_a = strength
print('Part1:', puzzle.answer_a)

print('\n'.join(''.join(row) for row in board))

puzzle.answer_b = 'PGHFGLUG'
print('Part2:', puzzle.answer_b)
