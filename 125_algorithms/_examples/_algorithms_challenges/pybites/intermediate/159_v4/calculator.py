import operator

OPS = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}


def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    if not any([op in calculation for op in OPS]):
        raise ValueError

    # assume op is good and split the string
    args = calculation.split()

    if len(args) != 3:
        raise ValueError

    a, op, b = args

    # convert to int raising error. Note, int does this
    a, b = (int(x) for x in (a, b))

    if b == 0 and op == '/':
        raise ValueError

    return OPS[op](a, b)
