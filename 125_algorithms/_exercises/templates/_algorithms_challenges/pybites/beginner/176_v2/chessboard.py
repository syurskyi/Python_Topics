____ i.. _______ cycle
WHITE, BLACK = ' ', '#'


___ create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

    
    c1 = cycle(f"{WHITE}{BLACK}")
    c2 = cycle(f"{BLACK}{WHITE}")

    c = c1
    ___ row __ r..(size):
        ___ col __ r..(size):
            print(next(c),end='')
        print()
        

        __ c __ c1:
            c = c2
        ____:
            c = c1



__ _______ __ _______


    create_chessboard()


