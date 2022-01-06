# _______ a__
#
#
# ___ calc_bmi weight, length
#     """Provided/DONE:
#        Calc BMI give a weight in kg and length in cm, return the BMI
#        rounded on 2 decimals"""
#     bmi  i.. ? / i.. ? / 100) ** 2)
#     r.. r.. ? 2
#
#
# ___ create_parser
#     """TODO:
#        Create an ArgumentParser adding the right arguments to pass the tests,
#        returns a argparse.ArgumentParser object"""
#     my_parser  a__.A.. prog='bmi.py',
#                                         description='Calculate your BMI.')
#     ?.a.. '-w',
#                        '--weight',
#                        a.._'store',
#                        h.._'Your weight in kg')
#     ?.a.. '-l',
#                        '--length',
#                        a.._'store',
#                        h.._'Your length in cm')
#     #print(my_parser.parse_args())
#     r.. ?
#
#
# ___ handle_args args_ N..
#     """Provided/DONE:
#        Call calc_bmi with provided args object.
#        If args are not provided get them from create_parser"""
#     __ args __ N..
#         parser  ?
#         args  ?.p..
#
#     __ ?.weight a.. ?.l..
#         bmi  ? ?.w.. ?.l..
#         print _*Your BMI is: ?
#     ____:
#         # could enforce SystemExit in create_parser/add_argument, but argparse
#         # docs are not clear how to do it, so raising the exception here manually
#         r.. S..
#
#
# __ _____ __ _____
#     ?