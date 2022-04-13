# _______ a__
# ____ f.. _______ r..
# _______ o..
#
# operations d..a.._s..,
#                   s.._l.... items r.. ?.s.. ?
#                   m.._l.... items r.. ?.m.. ?
#                   d.._l.... items r.. ?.t.. ?
#
#
# ___ calculator operation numbers
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#     func o__.g.. ?.l..
#     __ n.. ?
#         r.. V...('Invalid operation')
#
#     numbers f__ num ___ ? __ ?
#     r.. r.. ? ? 2
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
#     parser a__.A..(d.._'A simple calculator')
#     ?.a.. '-a', '--add', nargs='+', h.._"Sums numbers")
#     ?.a.. '-s', '--sub', nargs='+', h.._"Subtracts numbers")
#     ?.a.. '-m', '--mul', nargs='+', h.._"Multiplies numbers")
#     ?.a.. '-d', '--div', nargs='+', h.._"Divides numbers")
#     r.. ?
#
#
# ___ call_calculator args_N.. stdout_F..
#     """Provided/done:
#        Calls calculator with provided args object.
#        If args are not provided get them via create_parser,
#        if stdout is True print the result"""
#     parser ?
#
#     __ args __ N..
#         ? ?.p..
#
#     # taking the first operation in args namespace
#     # if combo, e.g. -a and -s, take the first one
#     ___ operation numbers __ v.. ? .i..
#         __ ? __ N..
#             _____
#
#         ___
#             res c.. o.. n..
#         ______ Z..
#             > 0
#
#         __ s..
#             print ?
#
#         r.. ?
#
#
# __ _____ __ _____
#     ? s.._T..