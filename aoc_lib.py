import parse


def findall(pat, s):
    return [res.fixed[0] for res in parse.findall(pat, s)]
