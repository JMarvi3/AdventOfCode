from current_puzzle import current_puzzle
from copy import deepcopy

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('4.example').read()


def test_board(f):
    return any(all(f[i][j] == False for i in range(5)) for j in range(5)) or \
           any(all(f[j][i] == False for i in range(5)) for j in range(5))


def dab(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = False


def play(boards, nums, part2=False):
    all_boards = set(range(len(boards)))
    for num in nums:
        for board_num in set(all_boards):
            board = boards[board_num]
            dab(board, num)
            if test_board(board):
                if not part2:
                    return num, board
                all_boards.remove(board_num)
        if not all_boards:
            return num, board


input = input_data.split('\n\n')

boards = []
for board_s in input[1:]:
    boards.append([list(map(int, line.split())) for line in board_s.splitlines()])

nums = list(map(int, input[0].split(',')))

num, board = play(deepcopy(boards), nums)
total = sum(board[i][j] for i in range(5) for j in range(5))
puzzle.answer_a = num * total
print('Part1:', puzzle.answer_a)

num, board = play(boards, nums, part2=True)
total = sum(board[i][j] for i in range(5) for j in range(5))
puzzle.answer_b = total * num
print('Part2:', puzzle.answer_b)
