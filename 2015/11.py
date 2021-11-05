from current_puzzle import current_puzzle


def fix_pass(s):
    result = ''
    for i in range(len(s)):
        c = s[i]
        if c in 'iol':
            return result + chr(ord(c)-1) + 'z' * (len(s)-i-1)
        else:
            result += c
    return result


def next_pass(s):
    for i in range(len(s)-1, -1, -1):
        if s[i] != 'z':
            return s[:i] + chr(ord(s[i]) + 1) + 'a' * (len(s)-i-1)


def pass_is_good(s):
    streak = False
    pairs = 0
    prev = ''
    count = 0
    for i in range(len(s)):
        if s[i] in 'iol':
            return False
        if not streak and i < len(s)-2 and ord(s[i]) + 1 == ord(s[i+1]) and ord(s[i+1]) + 1 == ord(s[i+2]):
            streak = True
            if pairs >= 2:
                return True
        if count == 0:
            prev = s[i]
            count = 1
        elif s[i] == prev:
            count += 1
        else:
            if count >= 2:
                pairs += 1
                if streak and pairs >= 2:
                    return True
            count = 1
            prev = s[i]
    if count >= 2:
        pairs += 1
    return streak and pairs >= 2


puzzle = current_puzzle()
password = puzzle.input_data
password = fix_pass(password)

while True:
    password = next_pass(password)
    if pass_is_good(password):
        break


puzzle.answer_a = password
print('Part1:', puzzle.answer_a)

while True:
    password = next_pass(password)
    if pass_is_good(password):
        break

puzzle.answer_b = password
print('Part2:', puzzle.answer_b)
