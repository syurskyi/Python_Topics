import argparse
import functools

___ calculator(f, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    


    return round(functools.reduce(lambda x,y: f(x,y),numbers),2)



___ create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    ap = argparse.ArgumentParser("A simple calculator")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("-m",'--mul',action='store_true',help="Multiplies numbers")
    group.add_argument("-s",'--sub',action='store_true',help="Subtracts numbers")
    group.add_argument("-a",'--add',action='store_true',help="Sums numbers")
    group.add_argument("-d",'--div',action='store_true',help="Divides numbers")
    ap.add_argument('numbers',nargs='+',type=float)

    return ap


___ call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args is None:
        args = vars(parser.parse_args())
    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    else:
        args = vars(args)
    numbers = args['numbers']
    __ args['mul']:
        f = lambda x,y: x * y
    elif args['sub']:
        f = lambda x,y: x - y
    elif args['add']:
        f = lambda x,y: x + y
    elif args['div']:
        f = lambda x,y: x / y


    try:
        res = calculator(f,numbers)
    except ZeroDivisionError:
        res = 0


    __ stdout:
        print(res)

    return res



__ __name__ == '__main__':
    call_calculator(stdout=True)
