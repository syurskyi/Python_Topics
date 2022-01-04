_______ argparse
_______ functools

___ calculator(f, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    


    r.. round(functools.reduce(l.... x,y: f(x,y),numbers),2)



___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    ap = argparse.ArgumentParser("A simple calculator")
    group = ap.add_mutually_exclusive_group(required=T..)
    group.add_argument("-m",'--mul',action='store_true',help="Multiplies numbers")
    group.add_argument("-s",'--sub',action='store_true',help="Subtracts numbers")
    group.add_argument("-a",'--add',action='store_true',help="Sums numbers")
    group.add_argument("-d",'--div',action='store_true',help="Divides numbers")
    ap.add_argument('numbers',nargs='+',t..=float)

    r.. ap


___ call_calculator(args=N.., stdout=F..):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args __ N..
        args = vars(parser.parse_args())
    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    ____:
        args = vars(args)
    numbers = args['numbers']
    __ args['mul']:
        f = l.... x,y: x * y
    ____ args['sub']:
        f = l.... x,y: x - y
    ____ args['add']:
        f = l.... x,y: x + y
    ____ args['div']:
        f = l.... x,y: x / y


    try:
        res = calculator(f,numbers)
    except ZeroDivisionError:
        res = 0


    __ stdout:
        print(res)

    r.. res



__ __name__ __ '__main__':
    call_calculator(stdout=T..)
