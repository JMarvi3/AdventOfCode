from aocd.models import Puzzle


def test(s):
    brackets = 0
    good = False
    for i in range(len(s)-3):
        c = s[i]
        if c == '[':
            brackets += 1
        elif c == ']':
            brackets -= 1
        else:
            g = s[i:i+4]
            if '[' not in g and ']' not in g and g[0] != g[1] and g[1] == g[2] and g[0] == g[3]:
                if brackets > 0:
                    return False
                good = True
    return good


print(sum(test(line) for line in Puzzle(2016, 7).input_data.splitlines()))


def test2(s):
    brackets = 0
    inside = ''
    abas = set()
    for i in range(len(s)-2):
        c = s[i]
        if c == '[':
            brackets += 1
            inside += c
        elif c == ']':
            brackets -= 1
            inside += c
        else:
            if brackets:
                inside += c
            g = s[i:i+3]
            if not brackets and '[' not in g and ']' not in g and g[0] != g[1] and g[2] == g[0]:
                abas.add(g)
    for aba in abas:
        if aba[1] + aba[0] + aba[1] in inside:
            return True
    return False

tests = ['aba[bab]xyz','xyx[xyx]xyx','aaa[kek]eke','zazbz[bzb]cdb']
print(sum(test2(line) for line in Puzzle(2016, 7).input_data.splitlines()))
