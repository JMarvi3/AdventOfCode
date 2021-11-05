from aocd.models import Puzzle
from hashlib import md5
import time


def password_part1(s):
    index = 0
    result = ''
    init_hash = md5()
    init_hash.update(bytes(s, 'utf-8'))
    while True:
        h = init_hash.copy()
        h.update(bytes(str(index), 'utf-8'))
        d = h.hexdigest()
        # d = digest(s, index)
        if d[:5] == '00000':
            result += d[5]
            if len(result) >= 8:
                break
        index += 1
    return result


def password_part2(s):
    index = 0
    result = ['-'] * 8
    init_hash = md5()
    init_hash.update(bytes(s, 'utf-8'))
    while True:
        h = init_hash.copy()
        h.update(bytes(str(index), 'utf-8'))
        d = h.hexdigest()
        if d[:5] == '00000':
            if '0' <= d[5] <= '7' and result[int(d[5])] == '-':
                result[int(d[5])] = d[6]
                if '-' not in result:
                    return ''.join(result)
        index += 1


def password_fast(s):
    index = 0
    part1_result = ''
    part2_result = ['-'] * 8
    init_hash = md5()
    init_hash.update(bytes(s, 'utf-8'))
    while True:
        h = init_hash.copy()
        h.update(bytes(str(index), 'utf-8'))
        d = h.hexdigest()
        if d[:5] == '00000':
            if len(part1_result) < 8:
                part1_result += d[5]
            if '0' <= d[5] <= '7' and part2_result[int(d[5])] == '-':
                part2_result[int(d[5])] = d[6]
                if '-' not in part2_result:
                    return part1_result, ''.join(part2_result)
        index += 1


start = time.perf_counter()
# print('part1:', password_part1(Puzzle(2016, 5).input_data), 'time:', time.perf_counter() - start)
# part1 = time.perf_counter()
# print('part2:', password_part2(Puzzle(2016, 5).input_data), 'time:', time.perf_counter() - part1)
# print('total time:', time.perf_counter() - start)

print('part1, part2:', password_fast(Puzzle(2016, 5).input_data), 'time:', time.perf_counter() - start)
