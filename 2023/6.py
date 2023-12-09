from current_puzzle import current_puzzle

def parse(line):
    return list(map(int, line.split(':')[1].split()))

def run(input_data):
    product = 1
    times, distances = map(parse, input_data.splitlines())
    for time, distance in zip(times, distances):
        win_count = 0
        for hold in range(time + 1):
            rest_time = time - hold
            new_distance = rest_time * hold
            if new_distance > distance:
                win_count += 1
        product *= win_count
    return product

puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = """Time:      7  15   30
# Distance:  9  40  200"""

puzzle.answer_a = run(input_data)
print('Part1:', puzzle.answer_a)

# input_data = """Time:      7  15   30
# Distance:  9  40  200"""

puzzle.answer_b = run(input_data.replace(' ', ''))
print('Part2:', puzzle.answer_b)
