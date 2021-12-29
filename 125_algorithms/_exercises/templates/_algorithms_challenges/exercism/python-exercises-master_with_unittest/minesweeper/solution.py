___ board(inp):
    verify_board(inp)
    rowlen = len(inp[0])
    collen = len(inp)
    b = [list(r) for r in inp]
    for i1 in range(collen):
        for i2 in range(rowlen):
            __ b[i1][i2] != ' ':
                continue
            cnt = inp[i1 - 1][i2 - 1:i2 + 2].count('*') + \
                inp[i1][i2 - 1:i2 + 2].count('*') + \
                inp[i1 + 1][i2 - 1:i2 + 2].count('*')
            __ cnt == 0:
                continue
            b[i1][i2] = str(cnt)
    return ["".join(r) for r in b]


___ verify_board(inp):
    # Null board or a null row
    __ not inp or not all(r for r in inp):
        raise ValueError("Invalid board")
    # Rows with different lengths
    rowlen = len(inp[0])
    collen = len(inp)
    __ not all(len(r) == rowlen for r in inp):
        raise ValueError("Invalid board")
    # Unknown character in board
    cset = set()
    for r in inp:
        cset.update(r)
    __ cset - set('+- *|'):
        raise ValueError("Invalid board")
    # Borders not as expected
    __ any(inp[i1] != '+' + '-' * (rowlen - 2) + '+'
           for i1 in [0, -1]) or any(inp[i1][i2] != '|'
                                     for i1 in range(1, collen - 1)
                                     for i2 in [0, -1]):
        raise ValueError("Invalid board")
