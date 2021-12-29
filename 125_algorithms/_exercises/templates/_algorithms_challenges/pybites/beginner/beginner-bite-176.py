WHITE, BLACK = ' ', '#'


___ create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(0, size):
        __ row % 2 == 0:
            for column in range(0, size):
                __ column % 2 == 0:
                    print(WHITE, end ='')
                else:
                    print(BLACK, end ='')
        else:
            for column in range(0, size):
                __ column % 2 == 0:
                    print(BLACK, end ='')
                else:
                    print(WHITE, end = '')
        print('\n')



create_chessboard(2)