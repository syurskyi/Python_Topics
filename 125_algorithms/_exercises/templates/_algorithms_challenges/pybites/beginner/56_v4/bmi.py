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
    parser = argparse.ArgumentParser(description='Calculate your BMI.')
    parser.add_argument('-w', '--weight', t..=i.., help='Your weight in kg')
    parser.add_argument('-l', '--length', t..=i.., help='Your length in cm')
    r.. parser



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


__ __name__ __ '__main__':
    handle_args()