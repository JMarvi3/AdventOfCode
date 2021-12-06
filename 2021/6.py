from current_puzzle import current_puzzle


def do_day(fish):
    new_fish = [0] * 9
    new_fish[8] = new_fish[6] = fish[0]
    for i in range(1, 9):
        new_fish[i-1] += fish[i]
    return new_fish


puzzle = current_puzzle()
input_data = puzzle.input_data
# input_data = '3,4,3,1,2'

fish = [0] * 9
for num in map(int, input_data.split(',')):
    fish[num] += 1

for _ in range(80):
    fish = do_day(fish)

puzzle.answer_a = sum(fish)
print('Part1:', puzzle.answer_a)

for _ in range(80, 256):
    fish = do_day(fish)

puzzle.answer_b = sum(fish)
print('Part2:', puzzle.answer_b)
