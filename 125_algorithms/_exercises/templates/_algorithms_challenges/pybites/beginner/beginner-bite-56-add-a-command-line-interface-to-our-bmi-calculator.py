'''
Complete create_parser below so that our BMI program can be called like this:

$ python bmi.py -h
usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

Calculate your BMI.

optional arguments:
  -h, --help            show this help message and exit
  -w WEIGHT, --weight WEIGHT
                        Your weight in kg
  -l LENGTH, --length LENGTH
                        Your length in cm

$ python bmi.py -w 80 -l 187
Your BMI is: 22.88
Please note that calc_bmi and handle_args are given, you only need to code create_parser!

We have two more Bites to practice argparse: 57 and 58.
'''


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
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--weight", help="Your weight in kg")
    parser.add_argument("-l", "--length", help="Your length in cm")
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
        print _*Your BMI is: {bmi}')
    ____:
        # could enforce SystemExit in create_parser/add_argument, but argparse
        # docs are not clear how to do it, so raising the exception here manually
        r.. SystemExit


__ _____ __ _____
    handle_args()