from operator ______ add, sub, mul, truediv


___ simple_calculator(calculation
    """Receives 'calculation' and returns the calculated result,
    """
    funcs = {'+': add, '-': sub, '*': mul, '/': truediv}
    try:
        a, op, b = calculation.split()
        a, b = int(a), int(b)
        r_ funcs[op](a, b)
    except Exception:
        raise ValueError
