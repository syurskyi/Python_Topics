_______ argparse


___ calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = i..(weight) / ((i..(length) / 100) ** 2)
    r.. round(bmi, 2)


___ create_parser
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
    my_parser = argparse.ArgumentParser(prog='bmi.py',
                                        description='Calculate your BMI.')
    my_parser.add_argument('-w',
                       '--weight',
                       action='store',
                       help='Your weight in kg')
    my_parser.add_argument('-l',
                       '--length',
                       action='store',
                       help='Your length in cm')
    #print(my_parser.parse_args())
    r.. my_parser


___ handle_args(args_ N..
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    __ args __ N..
        parser = create_parser()
        args = parser.parse_args()

    __ args.weight a.. args.length:
        bmi = calc_bmi(args.weight, args.length)
        print _*Your BMI is: {bmi}')
    ____:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        r.. SystemExit


__ _____ __ _____
    handle_args()