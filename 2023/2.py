from collections import Counter

from current_puzzle import current_puzzle

puzzle = current_puzzle()
input_data = puzzle.input_data

maximums = {'red': 12, 'green': 13, 'blue': 14}
valid_games = 0
for game in input_data.splitlines():
    game_valid = True
    id, cubes = game.split(': ')
    for round in cubes.split(';'):
        c = Counter()
        for num, color in map(str.split, round.split(', ')):
            c[color] += int(num)
        for color, count in c.items():
            if count > maximums[color]:
                game_valid = False
                break
    if game_valid:
        valid_games += int(id.split()[1])

puzzle.answer_a = valid_games
print('Part1:', puzzle.answer_a)

# input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

total_power = 0
for game in input_data.splitlines():
    all_c = Counter()
    game_valid = True
    id, cubes = game.split(': ')
    for round in cubes.split(';'):
        c = Counter()
        for num, color in map(str.split, round.split(', ')):
            c[color] += int(num)
        for color, count in c.items():
            all_c[color] = max(all_c[color], count)
    power = 1
    for num in all_c.values():
        power *= num
    total_power += power
print(total_power)
puzzle.answer_b = total_power
print('Part2:', puzzle.answer_b)
