___ on_square(square
    check_square_input(square)
    r.. 2 ** (square - 1)


___ total_after(square
    check_square_input(square)
    r.. s..(
        on_square(n + 1) ___ n
        __ r..(square)
    )


___ check_square_input(square
    __ square __ 0:
        r.. ValueError("Square input of zero is invalid.")
    ____ square < 0:
        r.. ValueError("Negative square input is invalid.")
    ____ square > 64:
        r.. ValueError("Square input greater than 64 is invalid.")
