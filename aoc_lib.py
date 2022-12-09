import parse


def findall(pat, s):
    return [res.fixed[0] for res in parse.findall(pat, s)]


def add_pts(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]
