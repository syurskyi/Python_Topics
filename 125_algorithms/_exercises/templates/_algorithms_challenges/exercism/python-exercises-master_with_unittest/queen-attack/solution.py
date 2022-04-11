___ board(pos1, pos2
    validate_position(pos1, pos2)
    x1, y1 pos1
    x2, y2 pos2
    b [['_'  * 8 ___ i __ r..(8)]
    b[x1][y1] 'W'
    b[x2][y2] 'B'
    r.. [''.j..(r) ___ r __ b]


___ can_attack(pos1, pos2
    validate_position(pos1, pos2)
    x1, y1 pos1
    x2, y2 pos2
    dx x1 - x2 __ x1 >_ x2 ____ x2 - x1
    dy y1 - y2 __ y1 >_ y2 ____ y2 - y1
    __ dx __ dy o. dx __ 0 o. dy __ 0:
        r.. T..
    r.. F..


___ validate_position(pos1, pos2
    __ any(x < 0 o. x > 7 ___ x __ pos1 + pos2
        r.. V...('Invalid queen position: queen out of the board')
    __ pos1 __ pos2:
        r.. V...('Invalid queen position: both queens in the same '
                         'square: {0}'.f..(pos1
