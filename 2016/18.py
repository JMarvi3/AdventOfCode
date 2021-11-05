from aocd.models import Puzzle


def next_row(row):
    row = '.' + row + '.'
    result = []
    for i in range(1, len(row)-1):
        result.append('^' if row[i-1:i+2] in ['^^.', '.^^', '^..', '..^'] else '.')
    return ''.join(result)


row = Puzzle(2016, 18).input_data
count = 0
for i in range(40):
    count += row.count('.')
    row = next_row(row)

print(count)

for i in range(400000 - 40):
    count += row.count('.')
    row = next_row(row)

print(count)
