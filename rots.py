from numpy import array, identity

# https://www.euclideanspace.com/maths/discrete/groups/categorise/finite/cube/index.htm
perms = ['x', 'y', 'xx', 'xy', 'yx', 'yy', 'xxx', 'xxy', 'xyx', 'xyy', 'yxx', 'yyx', 'yyy',
          'xxxy', 'xxyx', 'xxyy', 'xyxx', 'xyyy', 'yxxx', 'yyyx', 'xxxyx', 'xyxxx', 'xyyyx']
rotations = {'x': array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]), 'y': array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])}
possible_rots = None


def get_orthogonal_rotation_matrices():
    rots = [identity(3)]
    for perm in perms:
        m = identity(3)
        for c in perm:
            m = rotations[c] @ m
        rots.append(m)
    return rots


def apply_int_rot(v, i):
    global possible_rots
    if possible_rots is None:
        possible_rots = get_orthogonal_rotation_matrices()
    if i < 0 or i >= len(possible_rots) or len(v) != 3:
        raise ValueError
    return tuple(map(int, possible_rots[i] @ v))
