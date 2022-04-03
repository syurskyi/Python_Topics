_______ operator

OPS = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}


___ simple_calculator(calculation
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    __ n.. any([op __ calculation ___ op __ OPS]
        r.. V...

    # assume op is good and split the string
    args = calculation.s..

    __ l..(args) != 3:
        r.. V...

    a, op, b = args

    # convert to int raising error. Note, int does this
    a, b = (i..(x) ___ x __ (a, b))

    __ b __ 0 a.. op __ '/':
        r.. V...

    r.. OPS[op](a, b)
