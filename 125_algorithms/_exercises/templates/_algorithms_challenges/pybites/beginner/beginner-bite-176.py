WHITE, BLACK = ' ', '#'


___ create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    ___ row __ r..(0, size):
        __ row % 2 __ 0:
            ___ column __ r..(0, size):
                __ column % 2 __ 0:
                    print(WHITE, end ='')
                ____:
                    print(BLACK, end ='')
        ____:
            ___ column __ r..(0, size):
                __ column % 2 __ 0:
                    print(BLACK, end ='')
                ____:
                    print(WHITE, end = '')
        print('\n')



create_chessboard(2)