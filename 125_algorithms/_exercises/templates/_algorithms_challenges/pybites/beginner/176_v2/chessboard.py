from itertools import cycle
WHITE, BLACK = ' ', '#'


___ create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""

    
    c1 = cycle(f"{WHITE}{BLACK}")
    c2 = cycle(f"{BLACK}{WHITE}")

    c = c1
    for row in range(size):
        for col in range(size):
            print(next(c),end='')
        print()
        

        __ c __ c1:
            c = c2
        else:
            c = c1



__ __name__ == "__main__":


    create_chessboard()


