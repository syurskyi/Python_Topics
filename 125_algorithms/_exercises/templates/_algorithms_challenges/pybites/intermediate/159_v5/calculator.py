____ operator _______ add, sub, mul, truediv


___ simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,
    """
    funcs = {'+': add, '-': sub, '*': mul, '/': truediv}
    try:
        a, op, b = calculation.s..
        a, b = i..(a), i..(b)
        r.. funcs[op](a, b)
    except Exception:
        raise ValueError
