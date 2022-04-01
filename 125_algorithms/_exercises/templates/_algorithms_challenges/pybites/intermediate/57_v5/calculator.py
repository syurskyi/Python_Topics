_______ a__


___ calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    ops = {'add': l.... x: x[0] + x[1],
           'sub': l.... x: x[0] - x[1],
           'mul': l.... x: x[0] * x[1],
           'div': l.... x: x[0] / x[1]
           }
    __ isi..(numbers, i..):
        numbers = [numbers]
    res = f__(numbers[0])
    ___ num __ numbers[1:]:
        res = ops[operation]([res, f__(num)])
    r.. r..(res,2)


___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = a__.A..(d.._'A simple calculator')
    parser.a..('-a', '--add', t..=s.., nargs='+', h.._'Sums numbers')
    parser.a..('-s', '--sub', t..=s.., nargs='+', h.._'Subtracts numbers')
    parser.a..('-m', '--mul', t..=s.., nargs='+', h.._'Multiplies numbers')
    parser.a..('-d', '--div', t..=s.., nargs='+', h.._'Divides numbers')
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
