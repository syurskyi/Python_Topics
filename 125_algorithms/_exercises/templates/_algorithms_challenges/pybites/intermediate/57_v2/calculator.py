_______ a__
_______ f..

___ calculator(f, numbers
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    


    r.. r..(f...r.. l.... x,y: f(x,y),numbers),2)



___ create_parser
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    ap = a__.A..("A simple calculator")
    group = ap.add_mutually_exclusive_group(required=T..)
    group.a..("-m",'--mul',a.._'store_true',h.._"Multiplies numbers")
    group.a..("-s",'--sub',a.._'store_true',h.._"Subtracts numbers")
    group.a..("-a",'--add',a.._'store_true',h.._"Sums numbers")
    group.a..("-d",'--div',a.._'store_true',h.._"Divides numbers")
    ap.a..('numbers',nargs='+',t..=f__)

    r.. ap


___ call_calculator(args=N.., stdout=F..
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    __ args __ N..
        args = vars(parser.parse_args
    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    ____
        args = vars(args)
    numbers = args 'numbers'
    __ args 'mul' :
        f = l.... x,y: x * y
    ____ args 'sub' :
        f = l.... x,y: x - y
    ____ args 'add' :
        f = l.... x,y: x + y
    ____ args 'div' :
        f = l.... x,y: x / y


    ___
        res = calculator(f,numbers)
    ______ ZeroDivisionError:
        res = 0


    __ stdout:
        print(res)

    r.. res



__ _____ __ _____
    call_calculator(stdout=T..)
