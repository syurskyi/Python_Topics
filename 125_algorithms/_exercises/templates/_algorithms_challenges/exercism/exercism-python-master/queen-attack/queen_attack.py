"""Queen chess moves"""

___ validate(func
    """Ensures valid chess positions"""
    ___ chess_checker(black, white
        """Ensures valid chess positions"""
        __ min(black + white) < 0 or \
           max(black + white) > 7 or \
           black __ white:
            raise ValueError
        r_ func(black, white)
    r_ chess_checker

@validate
___ board(white, black
    """Prints a board with the queens locations"""
    chess = [["_"] * 8 for _ in range(8)]
    for char, (i, j) in (("W", white), ("B", black)):
        chess[i][j] = char
    r_ [''.join(row) for row in chess]

@validate
___ can_attack(black, white
    """Checks if the two queens can attack eachother"""
    diff = [abs(b - w) for b, w in zip(black, white)]
    r_ diff[0] __ diff[1] or min(diff) __ 0
