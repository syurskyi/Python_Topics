_______ argparse
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
    func = operations.get(operation.lower())
    __ n.. func:
        r.. ValueError('Invalid operation')

    numbers = [float(num) ___ num __ numbers]
    r.. round(func(numbers), 2)


___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument('-a', '--add', nargs='+', help="Sums numbers")
    parser.add_argument('-s', '--sub', nargs='+', help="Subtracts numbers")
    parser.add_argument('-m', '--mul', nargs='+', help="Multiplies numbers")
    parser.add_argument('-d', '--div', nargs='+', help="Divides numbers")
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