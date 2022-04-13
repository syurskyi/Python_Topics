# _______ a__
#
#
# ___ calculator operation numbers
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#     ops 'add': l.... x ? 0 + ? 1
#            'sub': l.... x ?0  - ? 1
#            'mul': l.... x ?0  * ? 1
#            'div': l.... x ?0  / ? 1
#
#     __ isi.. ?, i..
#         n.. ?
#     res f__ ? 0
#     ___ num __ ? 1|
#         res o.. o.. ? f__ ?
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
#     parser a__.A.. d.._'A simple calculator'
#     ?.a.. '-a' '--add' t.._s.. nargs_'+' h.._'Sums numbers'
#     ?.a.. '-s' '--sub' t.._s.. nargs_'+' h.._'Subtracts numbers'
#     ?.a.. '-m' '--mul' t.._s.. nargs_'+' h.._'Multiplies numbers'
#     ?.a.. '-d' '--div' t.._s.. nargs_'+' h.._'Divides numbers'
#     r.. ?
#
#
# ___ call_calculator args=N.., stdout=F..
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
#         __ n.. __ N..
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
#         r.. ?
#
#
# __ _____ __ _____
#     ? s.._T..
