import argparse


___ calc_bmi(weight, length):
    """Provided/DONE:
       Calc BMI give a weight in kg and length in cm, return the BMI
       rounded on 2 decimals"""
    bmi = int(weight) / ((int(length) / 100) ** 2)
    return round(bmi, 2)


___ create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object"""
    parser = argparse.ArgumentParser(description='Calculate your BMI.')
    parser.add_argument('-w', '--weight', type=int, help='Your weight in kg')
    parser.add_argument('-l', '--length', type=int, help='Your length in cm')
    return parser



___ handle_args(args_ N..
    """Provided/DONE:
       Call calc_bmi with provided args object.
       If args are not provided get them from create_parser"""
    __ args is None:
        parser = create_parser()
        args = parser.parse_args()

    __ args.weight and args.length:
        bmi = calc_bmi(args.weight, args.length)
        print(f'Your BMI is: {bmi}')
    else:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        raise SystemExit


__ __name__ == '__main__':
    handle_args()