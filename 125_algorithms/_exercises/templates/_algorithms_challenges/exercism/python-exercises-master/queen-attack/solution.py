___ board(pos1, pos2
    validate_position(pos1, pos2)
    x1, y1 = pos1
    x2, y2 = pos2
    b = [['_'] * 8 for i in range(8)]
    b[x1][y1] = 'W'
    b[x2][y2] = 'B'
    r_ [''.join(r) for r in b]


___ can_attack(pos1, pos2
    validate_position(pos1, pos2)
    x1, y1 = pos1
    x2, y2 = pos2
    dx = x1 - x2 __ x1 >= x2 else x2 - x1
    dy = y1 - y2 __ y1 >= y2 else y2 - y1
    __ dx __ dy or dx __ 0 or dy __ 0:
        r_ True
    r_ False


___ validate_position(pos1, pos2
    __ any(x < 0 or x > 7 for x in pos1 + pos2
        raise ValueError('Invalid queen position: queen out of the board')
    __ pos1 __ pos2:
        raise ValueError('Invalid queen position: both queens in the same '
                         'square: {0}'.format(pos1))
