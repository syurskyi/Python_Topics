WHITE, BLACK = ' ', '#'


___ create_chessboard(size=8
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    outstr, outboard = '', ''
    ___ i __ r..(size
        __ i % 2:
            outstr += BLACK
        ____:
            outstr += WHITE
    ___ j __ r..(size
        __ n.. (j % 2
            outboard += outstr+'\n'
        ____:
            outboard += outstr[::-1]+'\n'
    print(outboard)

create_chessboard(4)