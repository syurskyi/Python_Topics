___ board(inp
    verify_board(inp)
    rowlen l..(inp 0
    collen l..(inp)
    b [l..(r) ___ r __ inp]
    ___ i1 __ r..(collen
        ___ i2 __ r..(rowlen
            __ b[i1][i2] !_ ' ':
                _____
            cnt inp[i1 - 1][i2 - 1:i2 + 2].c.. '*') + \
                inp[i1][i2 - 1:i2 + 2].c.. '*') + \
                inp[i1 + 1][i2 - 1:i2 + 2].c.. '*')
            __ cnt __ 0:
                _____
            b[i1][i2] s..(cnt)
    r.. ["".j..(r) ___ r __ b]


___ verify_board(inp
    # Null board or a null row
    __ n.. inp o. n.. a..(r ___ r __ inp
        r.. V...("Invalid board")
    # Rows with different lengths
    rowlen l..(inp 0
    collen l..(inp)
    __ n.. a..(l..(r) __ rowlen ___ r __ inp
        r.. V...("Invalid board")
    # Unknown character in board
    cset s..()
    ___ r __ inp:
        cset.update(r)
    __ cset - s..('+- *|'
        r.. V...("Invalid board")
    # Borders not as expected
    __ any(inp[i1] !_ '+' + '-' * (rowlen - 2) + '+'
           ___ i1 __ [0, -1]) o. any(inp[i1][i2] !_ '|'
                                     ___ i1 __ r..(1, collen - 1)
                                     ___ i2 __ [0, -1]
        r.. V...("Invalid board")
