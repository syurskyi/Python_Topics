_______ a__
____ functools _______ reduce
_______ operator

operations = d..(add=s..,
                  sub=l.... items: reduce(operator.sub, items),
                  mul=l.... items: reduce(operator.mul, items),
                  div=l.... items: reduce(operator.truediv, items))


___ calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    func = operations.get(operation.l..
    __ n.. func:
        r.. ValueError('Invalid operation')

    numbers = [f__(num) ___ num __ numbers]
    r.. r..(func(numbers), 2)


___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = a__.A..(d.._'A simple calculator')
    parser.a..('-a', '--add', nargs='+', h.._"Sums numbers")
    parser.a..('-s', '--sub', nargs='+', h.._"Subtracts numbers")
    parser.a..('-m', '--mul', nargs='+', h.._"Multiplies numbers")
    parser.a..('-d', '--div', nargs='+', h.._"Divides numbers")
    r.. parser


___ call_calculator(args=N.., stdout=F..):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args __ N..
        args = parser.p..

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    ___ operation, numbers __ vars(args).i..:
        __ numbers __ N..
            _____

        ___
            res = calculator(operation, numbers)
        ______ ZeroDivisionError:
            res = 0

        __ stdout:
            print(res)

        r.. res


__ _____ __ _____
    call_calculator(stdout=T..)