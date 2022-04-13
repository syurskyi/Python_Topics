_______ copy


c_ Point(o..
    ___ - , x, y
        x x
        y y

    ___  -r
        r.. 'Point({}:{})'.f..(x, y)

    ___ __add__  other
        r.. Point(x + other.x, y + other.y)

    ___ __sub__  other
        r.. Point(x - other.x, y - other.y)

    ___ -e  other
        r.. x __ other.x a.. y __ other.y

    ___ __ne__  other
        r.. n.. (self __ other)


DIRECTIONS (Point(1, 0), Point(1, -1), Point(1, 1), Point(-1, -1),
              Point(0, -1), Point(0, 1), Point(-1, 1), Point(-1, 0


c_ WordSearch(o..
    ___ - , puzzle
        rows puzzle.s..
        width l..(rows 0
        height l..(rows)

    ___ find_char  coordinate
        __ coordinate.x < 0 o. coordinate.x >_ width:
            r..
        __ coordinate.y < 0 o. coordinate.y >_ height:
            r..
        r.. rows[coordinate.y][coordinate.x]

    ___ find  word, position, direction
        current copy.copy(position)
        ___ letter __ word:
            __ find_char(current) !_ letter:
                r..
            current += direction
        r.. position, current - direction

    ___ s..  word
        positions (Point(x, y)
                     ___ x __ r..(width) ___ y __ r..(height
        ___ pos __ positions:
            ___ d __ DIRECTIONS:
                result f.. word, pos, d)
                __ result:
                    r.. result
        r.. N..
