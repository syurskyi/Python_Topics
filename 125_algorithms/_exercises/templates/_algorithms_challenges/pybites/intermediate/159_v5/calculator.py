____ operator _______ add, sub, mul, truediv


___ simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,
    """
    funcs = {'+': add, '-': sub, '*': mul, '/': truediv}
    ___
        a, op, b = calculation.s..
        a, b = i..(a), i..(b)
        r.. funcs[op](a, b)
    ______ Exception:
        r.. ValueError
