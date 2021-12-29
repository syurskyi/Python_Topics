___ create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    WHITE, BLACK = ' ', '#'
    dup = int(size / 2)
    ___ row __ r..(size):
        __ row % 2 __ 0:
            odd_row = (WHITE + BLACK) * dup
            print(odd_row)
        ____:
            even_row = (BLACK + WHITE) * dup
            print(even_row)