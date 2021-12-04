from current_puzzle import current_puzzle
from copy import deepcopy

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = open('4.example').read()


def test_board(board):
    return any(all(board[i][j] is False for i in range(5)) or
               all(board[j][i] is False for i in range(5))
               for j in range(5))


def dab(board, num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = False


def play(boards, nums, part2=False):
    board = None
    all_boards = set(range(len(boards)))
    for num in nums:
        for board_num in set(all_boards):
            board = boards[board_num]
            dab(board, num)
            if test_board(board):
                if not part2:
                    return num * sum(map(sum, board))
                all_boards.remove(board_num)
        if not all_boards:
            return num * sum(map(sum, board))


input = input_data.split('\n\n')

boards = []
for board_s in input[1:]:
    boards.append([list(map(int, line.split())) for line in board_s.splitlines()])

nums = list(map(int, input[0].split(',')))

puzzle.answer_a = play(deepcopy(boards), nums)
print('Part1:', puzzle.answer_a)

puzzle.answer_b = play(boards, nums, part2=True)
print('Part2:', puzzle.answer_b)
