c_ Point(o..
    ___ - , x, y
        x x
        y y

    ___  -r
        r.. 'Point({}:{})'.f..(x, y)

    ___ -a  other
        r.. Point(x + other.x, y + other.y)

    ___ -s  other
        r.. Point(x - other.x, y - other.y)

    ___ -e  other
        r.. x __ other.x a.. y __ other.y

    ___ __ne__  other
        r.. n..(self __ other)


c_ WordSearch(o..
    ___ - , puzzle
        p..

    ___ s..  word
        r.. N..
