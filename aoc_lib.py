import string
from typing import List, Callable

import parse

int_pat = parse.compile('{:d}')


def findall(pat, s): return [res.fixed[0] for res in parse.findall(pat, s)]


def findall_ints(s): return findall(int_pat, s)


def add_pts(p1, p2): return tuple(map(sum, zip(p1, p2)))


def bubble_sort(l: List, compare: Callable):
    while True:
        done = True
        for i in range(1, len(l)):
            if compare(l[i - 1], l[i]) > 0:
                l[i - 1], l[i] = l[i], l[i - 1]
                done = False
        if done:
            return


add_pts3 = add_pts

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
lower_alpha = string.ascii_lowercase
upper_alpha = string.ascii_uppercase
alpha = string.ascii_letters
num = string.digits
alnum = alpha + num
