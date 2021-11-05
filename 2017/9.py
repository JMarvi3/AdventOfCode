from aocd.models import Puzzle

data = Puzzle(2017, 9).input_data.strip()

index = group = score = total_garbage = 0
garbage = False
while True:
    c = data[index]
    if c == '!':
        index += 1
    elif garbage:
        if c == '>':
            garbage = False
        else:
            total_garbage += 1
    elif c == '{':
        group += 1
        score += group
    elif c == '}':
        group -= 1
        if group == 0:
            break
    elif c == '<':
        garbage = True
    index += 1

print('Part1:', score)
print('Part2:', total_garbage)
