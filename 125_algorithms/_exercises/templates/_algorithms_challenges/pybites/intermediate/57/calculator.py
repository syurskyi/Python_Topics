# _______ a__
#
# ___ calculator operation numbers
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#     print ? ?
#     total 0
#     __ operation __ 'add'
#         t.. f__ ? 0
#         ___ i __ ? 1|
#             total ? + f__ ?
#     ____ o.. __ 'sub'
#         t.. f__ ? 0
#         ___ i __ ? 1|
#             t.. ? - f__ ?
#     ____ o.. __ 'mul'
#         t.. f__ ? 0
#         print ?
#         ___ i __ ? 1|
#             t.. ? * f__ ?
#             print ?
#     ____ o.. __ 'div':
#         t.. f__ ? 0
#         ___ i __ ? 1|
#             t.. ? / f__ ?
#     print t.. t..
#     r.. r.. ? 2
#
#
# ___ create_parser
#     """TODO 2:
#        Create an ArgumentParser object:
#        - have one operation argument,
#        - have one or more integers that can be operated on.
#        Returns a argparse.ArgumentParser object.
#
#        Note that type=float times out here so do the casting in the calculator
#        function above!"""
#     my_parser a__.A.. d.._'A simple calculator'
#     ?.a.. '-a',
#                        '--add',
#                        a.._'store', nargs='+',
#                        h.._'Sums numbers'
#     ?.a.. '-s',
#                        '--sub',
#                        a.._'store', nargs='+',
#                        h.._'Subtracts numbers'
#     ?.a.. '-m',
#                        '--mul',
#                        a.._'store', nargs='+',
#                        h.._'Multiplies numbers'
#     ?.a.. '-d',
#                        '--div',
#                        a.._'store', nargs='+',
#                        h.._'Divides numbers'
#     #print(my_parser.parse_args())
#     r.. ?
#
#
# ___ call_calculator args=N.. stdout=F..
#     """Provided/done:
#        Calls calculator with provided args object.
#        If args are not provided get them via create_parser,
#        if stdout is True print the result"""
#     parser ?
#
#     __ a.. __ N..
#         args ?.p..
#
#     # taking the first operation in args namespace
#     # if combo, e.g. -a and -s, take the first one
#     ___ operation numbers __ v.. a.. .i..
#         #print(operation, numbers)
#         __ ? __ N..
#             _____
#
#         ___
#             res c.. o.. n..
#         ______ Z..
#             ? 0
#
#         __ s..
#             print ?
#
#         r.. res
#
#
# __ _____ __ _____
#     call_calculator(stdout=T..)