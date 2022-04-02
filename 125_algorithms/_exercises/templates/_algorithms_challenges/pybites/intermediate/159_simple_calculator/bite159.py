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

    operation = {
        '+': (l.... x, y: x + y),
        '-': (l.... x, y: x - y),
        '*': (l.... x, y: x * y),
        '/': (l.... x, y: x / y)
        }

    ___
        x = i..(calculation.s.. [0])
        y = i..(calculation.s.. [2])
        operator = calculation.s.. [1]
        r.. operation[operator](i..(x), i..(y))
    
    ______ (ValueError, KeyError, ZeroDivisionError
        r.. ValueError
