___ on_square(square
    check_square_input(square)
    r_ 2 ** (square - 1)


___ total_after(square
    check_square_input(square)
    r_ sum(
        on_square(n + 1) for n
        in range(square)
    )


___ check_square_input(square
    __ square __ 0:
        raise ValueError("Square input of zero is invalid.")
    ____ square < 0:
        raise ValueError("Negative square input is invalid.")
    ____ square > 64:
        raise ValueError("Square input greater than 64 is invalid.")
