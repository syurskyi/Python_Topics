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

    operation = {
        '+': (lambda x, y: x + y), 
        '-': (lambda x, y: x - y),
        '*': (lambda x, y: x * y),
        '/': (lambda x, y: x / y)
        }

    try:
        x = int(calculation.split()[0])
        y = int(calculation.split()[2])
        operator = calculation.split()[1]
        return operation[operator](int(x), int(y))
    
    except (ValueError, KeyError, ZeroDivisionError):
        raise ValueError
