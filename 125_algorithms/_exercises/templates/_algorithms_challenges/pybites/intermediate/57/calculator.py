_______ argparse

___ calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    print(operation,numbers)
    total = 0
    __ operation __ 'add':
        total = float(numbers[0])
        ___ i __ numbers[1:]:
            total = total + float(i)
    ____ operation __ 'sub':
        total = float(numbers[0])
        ___ i __ numbers[1:]:
            total = total - float(i)
    ____ operation __ 'mul':
        total = float(numbers[0])
        print(total)
        ___ i __ numbers[1:]:
            total = total * float(i)
            print(total)
    ____ operation __ 'div':
        total = float(numbers[0])
        ___ i __ numbers[1:]:
            total = total / float(i)
    print(type(total))
    r.. round(total,2)


___ create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    my_parser = argparse.ArgumentParser(description='A simple calculator')
    my_parser.add_argument('-a',
                       '--add',
                       action='store', nargs='+',
                       help='Sums numbers')
    my_parser.add_argument('-s',
                       '--sub',
                       action='store', nargs='+',
                       help='Subtracts numbers')
    my_parser.add_argument('-m',
                       '--mul',
                       action='store', nargs='+',
                       help='Multiplies numbers')
    my_parser.add_argument('-d',
                       '--div',
                       action='store', nargs='+',
                       help='Divides numbers')
    #print(my_parser.parse_args())
    r.. my_parser


___ call_calculator(args=N.., stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args __ N..
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    ___ operation, numbers __ vars(args).items():
        #print(operation, numbers)
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
    call_calculator(stdout=True)