_______ a__
____ f.. _______ r..
____ operator _______ add, sub, mul, truediv


___ calculator(operation, numbers
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    OPS = {'add': add, 'sub': sub, 'mul': mul, 'div': truediv}
    r.. r..(r.. OPS[operation], map(f__, numbers, 2)


___ create_parser
    """Creates and returns and argument parser object with:
    - an opration argument
    - one or more numbers to operate on
    """
    parser = a__.A..(d.._'A simple calculator')
    parser.a..('-a', '--add', nargs='+',
                        h.._'Sums numbers')
    parser.a..('-s', '--sub', nargs='+',
                        h.._'Subtracts numbers')
    parser.a..('-m', '--mul', nargs='+',
                        h.._'Multiplies numbers')
    parser.a..('-d', '--div', nargs='+',
                        h.._'Divides numbers')

    r.. parser


___ call_calculator(args=N.., stdout=F..
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
