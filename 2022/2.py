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
    # return points[you] + (6 if to_win[them] == you else 3 if to_draw[them] == you else 0)
    if to_win[them] == you:
        return 6 + points[you]
    elif to_lose[them] == you:
        return points[you]
    else:
        return 3 + points[you]


score = sum(get_score(*play) for play in plays)

score = 0
for them, you in plays:
    if to_win[them] == you:
        score += 6
    elif to_draw[them] == you:
        score += 3
    score += points[you]

puzzle.answer_a = score
print('Part1:', puzzle.answer_a)

# correct_plays = {'X': to_lose, 'Y': to_draw, 'Z': to_win}
# score = sum(get_score(them, correct_plays[strategy][them]) for them, strategy in plays)

score = 0
for them, strategy in plays:
    if strategy == 'X':
        score += get_score(them, to_lose[them])
    elif strategy == 'Y':
        score += get_score(them, to_draw[them])
    else:
        score += get_score(them, to_win[them])

puzzle.answer_b = score
print('Part2:', puzzle.answer_b)
