from aocd.models import Puzzle

data = Puzzle(2017, 4).input_data.splitlines()

count = 0
for phrase in data:
    valid = True
    seen = set()
    for word in phrase.split():
        if word in seen:
            valid = False
            break
        seen.add(word)
    count += valid

print('Part1:', count)

count = 0
for phrase in data:
    valid = True
    seen = set()
    for word in phrase.split():
        word = ''.join(sorted(word))
        if word in seen:
            valid = False
            break
        seen.add(word)
    count += valid

print('Part2:', count)
