from aocd.models import Puzzle
import re
from collections import Counter


def decrypt(name, id):
    result = ''
    for c in name:
        if c == '-':
            result += ' '
        else:
            index = ord(c) - ord('a')
            index = (index + id) % 26
            result += chr(ord('a') + index)
    return result


pat = re.compile(r'((?:\w+-)+)(\d+)\[(.*)\]')
total = 0
part2 = None
for line in Puzzle(2016, 4).input_data.splitlines():
    name, id, checksum = pat.match(line).groups()
    id = int(id)
    counter = Counter(sorted(name.replace('-', '')))
    if ''.join(c for c, n in counter.most_common(5)) == checksum:
        total += id
        room_name = decrypt(name, id)
        if 'pole' in room_name:
            part2 = id

print('part1:', total)
print('part2:', part2)
