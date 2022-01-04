_______ argparse
____ functools _______ reduce
____ operator _______ add, sub, mul, truediv


___ calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    OPS = {'add': add, 'sub': sub, 'mul': mul, 'div': truediv}
    r.. round(reduce(OPS[operation], map(float, numbers)), 2)


___ create_parser
    """Creates and returns and argument parser object with:
    - an opration argument
    - one or more numbers to operate on
    """
    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument('-a', '--add', nargs='+',
                        help='Sums numbers')
    parser.add_argument('-s', '--sub', nargs='+',
                        help='Subtracts numbers')
    parser.add_argument('-m', '--mul', nargs='+',
                        help='Multiplies numbers')
    parser.add_argument('-d', '--div', nargs='+',
                        help='Divides numbers')

    r.. parser


___ call_calculator(args=N.., stdout=F..):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args __ N..
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    ___ operation, numbers __ vars(args).i..:
        __ numbers __ N..
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        __ stdout:
            print(res)

        r.. res


__ __name__ __ '__main__':
    call_calculator(stdout=T..)
