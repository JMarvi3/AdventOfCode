from current_puzzle import current_puzzle
import aoc_lib


def check_password(password, part2=False):
    prev_digit = 10
    counts = dict()
    while password:
        digit = password % 10
        if digit > prev_digit:
            return False
        counts[digit] = counts.get(digit, 0) + 1
        prev_digit = digit
        password //= 10
    return any(val >= 2 for val in counts.values()) if not part2 else (2 in counts.values())

puzzle = current_puzzle()
print(puzzle.title)
input_data = puzzle.input_data

start, finish = map(int, input_data.split('-'))
valid_count = sum(check_password(password) for password in range(start, finish+1))

puzzle.answer_a = valid_count
print('Part1:', puzzle.answer_a)
puzzle.answer_b = sum(check_password(password, part2=True) for password in range(start, finish+1))
print('Part2:', puzzle.answer_b)
