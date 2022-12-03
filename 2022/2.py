from current_puzzle import current_puzzle
import aoc_lib
to_win = dict(['CX', 'AY', 'BZ'])
to_draw = dict(['AX', 'BY', 'CZ'])
to_lose = dict(['BX', 'CY', 'AZ'])

# win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
# draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
points = {'X': 1, 'Y': 2, 'Z': 3}
puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data
# input_data = open('2.example').read()
plays = list(map(str.split, input_data.split('\n')))


def get_score(them, you):
    return points[you] + (6 if to_win[them] == you else 3 if to_draw[them] == you else 0)
    # if to_win[them] == you:
    #     return 6 + points[you]
    # elif to_lose[them] == you:
    #     return points[you]
    # else:
    #     return 3 + points[you]


score = sum(get_score(*play) for play in plays)
#
# score = 0
# for line in input_data.split('\n'):
#     him, you = line.split()
#     # print(score, him, you, end='')
#     if win[you] == him:
#         score += 6
#     elif draw[you] == him:
#         score += 3
#     score += shapes[you]
#     # print('', score)

puzzle.answer_a = score
print('Part1:', puzzle.answer_a)

correct_plays = {'X': to_lose, 'Y': to_draw, 'Z': to_win}
score = sum(get_score(them, correct_plays[you][them]) for them, you in plays)

# score = 0
#
# for line in input_data.split('\n'):
#     him, you = line.split()
#     if you == 'X':
#         score += shapes[to_lose[him]]
#     elif you == 'Y':
#         score += 3 + shapes[to_draw[him]]
#     else:
#         score += 6 + shapes[to_win[him]]
#
puzzle.answer_b = score
print('Part2:', puzzle.answer_b)
