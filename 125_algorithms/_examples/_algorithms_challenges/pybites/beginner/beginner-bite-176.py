WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(0, size):
        if row % 2 == 0:
            for column in range(0, size):
                if column % 2 == 0:
                    print(WHITE, end ='')
                else:
                    print(BLACK, end ='')
        else:
            for column in range(0, size):
                if column % 2 == 0:
                    print(BLACK, end ='')
                else:
                    print(WHITE, end = '')
        print('\n')



create_chessboard(2)