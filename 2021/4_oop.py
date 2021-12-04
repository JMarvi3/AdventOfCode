from current_puzzle import current_puzzle
from copy import deepcopy

puzzle = current_puzzle()
input_data = puzzle.input_data


# input_data = open('4.example').read()

class Board:
    def __init__(self, s):
        self.numbers = {int(num): (i, j) for i, row in enumerate(s.splitlines()) for j, num in enumerate(row.split())}
        assert len(self.numbers) == 25
        self.total = sum(self.numbers.keys())
        self.counts = [5] * 10

    def dab(self, num):
        if num in self.numbers:
            i, j = self.numbers[num]
            self.total -= num
            self.counts[i] -= 1
            self.counts[5 + j] -= 1
            return True
        return False

    def bingo(self):
        return 0 in self.counts


def play(boards, nums, part2=False):
    board: Board = None
    all_boards = set(range(len(boards)))
    for num in nums:
        for board_num in set(all_boards):
            board = boards[board_num]
            if board.dab(num) and board.bingo():
                if not part2:
                    return num * board.total
                all_boards.remove(board_num)
        if not all_boards:
            return num * board.total


input_lines = input_data.split('\n\n')

boards = list(map(Board, input_lines[1:]))
nums = list(map(int, input_lines[0].split(',')))

puzzle.answer_a = play(deepcopy(boards), nums)
print('Part1:', puzzle.answer_a)

puzzle.answer_b = play(boards, nums, part2=True)
print('Part2:', puzzle.answer_b)
