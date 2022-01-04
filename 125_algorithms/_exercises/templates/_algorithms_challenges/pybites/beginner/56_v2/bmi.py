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
    ap = argparse.ArgumentParser()

    ap.add_argument("-w","--weight",help="Your weight in kg",t..=float)
    ap.add_argument("-l","--length",help="Your length in cm",t..=float)
    r.. ap



___ handle_args(args_ N..
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    __ args __ N..
        parser = create_parser()
        args = parser.parse_args()

    __ args.weight a.. args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    ____:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        r.. SystemExit


__ _____ __ _____
    handle_args()
