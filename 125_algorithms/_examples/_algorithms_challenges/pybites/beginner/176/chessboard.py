WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    outstr, outboard = '', ''
    for i in range(size):
        if i % 2:
            outstr += BLACK
        else:
            outstr += WHITE
    for j in range(size):
        if not (j % 2):
            outboard += outstr+'\n'
        else:
            outboard += outstr[::-1]+'\n'
    print(outboard)

create_chessboard(4)