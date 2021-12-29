import argparse

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    print(operation,numbers)
    total = 0
    if operation == 'add':
        total = float(numbers[0])
        for i in numbers[1:]:
            total = total + float(i)
    elif operation == 'sub':
        total = float(numbers[0])
        for i in numbers[1:]:
            total = total - float(i)
    elif operation == 'mul':
        total = float(numbers[0])
        print(total)
        for i in numbers[1:]:
            total = total * float(i)
            print(total)
    elif operation == 'div':
        total = float(numbers[0])
        for i in numbers[1:]:
            total = total / float(i)
    print(type(total))
    return round(total,2)


def create_parser():
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
    return my_parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        #print(operation, numbers)
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)