___ board(inp
    verify_board(inp)
    rowlen = le.(inp[0])
    collen = le.(inp)
    b = [list(r) ___ r in inp]
    ___ i1 in range(collen
        ___ i2 in range(rowlen
            __ b[i1][i2] != ' ':
                continue
            cnt = inp[i1 - 1][i2 - 1:i2 + 2].count('*') + \
                inp[i1][i2 - 1:i2 + 2].count('*') + \
                inp[i1 + 1][i2 - 1:i2 + 2].count('*')
            __ cnt __ 0:
                continue
            b[i1][i2] = str(cnt)
    r_ ["".join(r) ___ r in b]


___ verify_board(inp
    # Null board or a null row
    __ not inp or not all(r ___ r in inp
        raise ValueError("Invalid board")
    # Rows with different lengths
    rowlen = le.(inp[0])
    collen = le.(inp)
    __ not all(le.(r) __ rowlen ___ r in inp
        raise ValueError("Invalid board")
    # Unknown character in board
    cset = set()
    ___ r in inp:
        cset.update(r)
    __ cset - set('+- *|'
        raise ValueError("Invalid board")
    # Borders not as expected
    __ any(inp[i1] != '+' + '-' * (rowlen - 2) + '+'
           ___ i1 in [0, -1]) or any(inp[i1][i2] != '|'
                                     ___ i1 in range(1, collen - 1)
                                     ___ i2 in [0, -1]
        raise ValueError("Invalid board")
