from aocd.models import Puzzle


def generate(s, l):
    while len(s) < l:
        result = []
        for i in range(len(s)-1, -1, -1):
            result.append('0' if s[i] == '1' else '1')
        s += '0' + ''.join(result)
    return s[:l]


def checksum(s):
    while len(s) % 2 == 0:
        c = []
        for i in range(0, len(s), 2):
            c.append('1' if s[i] == s[i+1] else '0')
        s = ''.join(c)
    return s


s = Puzzle(2016, 16).input_data
print('part1:', checksum(generate(s, 272)))
print('part2:', checksum(generate(s, 35651584)))
