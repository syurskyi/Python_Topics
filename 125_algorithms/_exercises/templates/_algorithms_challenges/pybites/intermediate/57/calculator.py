_______ a__

___ calculator(operation, numbers
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    print(operation,numbers)
    total = 0
    __ operation __ 'add':
        total = f__(numbers[0])
        ___ i __ numbers[1:]:
            total = total + f__(i)
    ____ operation __ 'sub':
        total = f__(numbers[0])
        ___ i __ numbers[1:]:
            total = total - f__(i)
    ____ operation __ 'mul':
        total = f__(numbers[0])
        print(total)
        ___ i __ numbers[1:]:
            total = total * f__(i)
            print(total)
    ____ operation __ 'div':
        total = f__(numbers[0])
        ___ i __ numbers[1:]:
            total = total / f__(i)
    print(t..(total))
    r.. r..(total,2)


___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    my_parser = a__.A..(d.._'A simple calculator')
    my_parser.a..('-a',
                       '--add',
                       a.._'store', nargs='+',
                       h.._'Sums numbers')
    my_parser.a..('-s',
                       '--sub',
                       a.._'store', nargs='+',
                       h.._'Subtracts numbers')
    my_parser.a..('-m',
                       '--mul',
                       a.._'store', nargs='+',
                       h.._'Multiplies numbers')
    my_parser.a..('-d',
                       '--div',
                       a.._'store', nargs='+',
                       h.._'Divides numbers')
    #print(my_parser.parse_args())
    r.. my_parser


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
        #print(operation, numbers)
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