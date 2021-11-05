from aocd.models import Puzzle
from hashlib import md5
import re
import time


def get_digest(salt, index, stretch=False):
    d = salt + str(index)
    for i in range(2017 if stretch else 1):
        m = md5()
        m.update(bytes(d, 'utf-8'))
        d = m.hexdigest()
    return d


def find(salt, stretch=False):
    triple_pat = re.compile(r'(.)\1\1')
    five_pat = re.compile(r'(.)\1\1\1\1')
    triples = []
    fives = []
    size = 1001
    for i in range(size):
        digest = get_digest(salt, i, stretch)
        triples.append(set(triple_pat.findall(digest)[:1]))
        fives.append(set(five_pat.findall(digest)))

    index = 0
    count = 0
    while count < 64:
        if triples[index % size]:
            for i in range(1, 1001):
                if triples[index % size] & fives[(index + i) % size]:
                    count += 1
                    if count == 64:
                        return index
                    break
        digest = get_digest(salt, index + size, stretch)
        triples[(index + size) % size] = set(triple_pat.findall(digest)[:1])
        fives[(index + size) % size] = set(five_pat.findall(digest))
        index += 1


start = time.perf_counter()
s = Puzzle(2016, 14).input_data
print('part1:', find(s), end='')
part1 = time.perf_counter()
print(f" ({round(part1 - start, 4)})")
print('part2:', find(s, stretch=True), end='')
end = time.perf_counter()
print(f" ({round(end - part1, 4)} / {round(end - start, 4)})")
