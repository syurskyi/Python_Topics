# _______ a__
# ____ f.. _______ r..
# ____ o.. _______ a.. s.. m.. t..
#
#
# ___ calculator operation numbers
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#     OPS  'add' ? 'sub' ? 'mul' ? 'div' ?
#     r.. r.. r.. ? ? m.. f__ ? 2
#
#
# ___ create_parser
#     """Creates and returns and argument parser object with:
#     - an opration argument
#     - one or more numbers to operate on
#     """
#     parser a__.A.. d.._'A simple calculator'
#     ?.a.. '-a', '--add', nargs='+',
#                         h.._'Sums numbers'
#     ?.a.. '-s', '--sub', nargs='+',
#                         h.._'Subtracts numbers'
#     ?.a.. '-m', '--mul', nargs='+',
#                         h.._'Multiplies numbers'
#     ?.a.. '-d', '--div', nargs='+',
#                         h.._'Divides numbers'
#
#     r.. ?
#
#
# ___ call_calculator a.._N.. s.._F..
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
#     ___ operation, numbers __ v.. ?.i..
#         __ ? __ N..
#             _____
#
#         ___
#             res c.. o.. n..
#         ______ Z..
#             ? 0
#
#         __ stdout
#             print ?
#
#         r.. ?
#
#
# __ _____ __ _____
#     ? s.._T..
