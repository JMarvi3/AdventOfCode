from aocd.models import Puzzle


def decode(s, nest=False):
    result = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            end = s[i:].index(')') + i  # s[end] == ')'
            a, b = list(map(int, s[i + 1:end].split('x')))
            if nest:
                result += decode(s[end + 1:end + 1 + a], nest) * b
            else:
                result += a * b
            i = end + 1 + a
        else:
            result += 1
            i += 1
    return result


# for s in ['ADVENT', 'A(1x5)BC', '(3x3)XYZ', 'A(2x2)BCD(2x2)EFG', '(6x1)(1x3)A', 'X(8x2)(3x3)ABCY']:
#     print(f"{s}: {decode(s)}")

s = Puzzle(2016, 9).input_data
print('part1:', decode(s))
print('part2:', decode(s, nest=True))
