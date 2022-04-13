# _______ a__
# _______ f..
#
# ___ calculator f numbers
#     """TODO 1:
#        Create a calculator that takes an operation and list of numbers.
#        Perform the operation returning the result rounded to 2 decimals"""
#
#
#
#     r.. r.. f...r.. l.... x,y| ? ? ? ? 2
#
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
#     ap a__.A..("A simple calculator")
#     group ?.a.. required=T..
#     ?.a.. "-m",'--mul',a.._'store_true' h.._"Multiplies numbers"
#     ?.a.. "-s",'--sub',a.._'store_true' h.._"Subtracts numbers"
#     ?.a.. "-a",'--add',a.._'store_true' h.._"Sums numbers"
#     ?.a.. "-d",'--div',a.._'store_true' h.._"Divides numbers"
#     ap.a..('numbers' nargs_'+' t.._f__
#
#     r.. ap
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
#         a.. v.. ?.p..
#     # taking the first operation in args namespace
#     # if combo, e.g. -a and -s, take the first one
#     ____
#         ? v.. ?
#     numbers ? 'numbers'
#     __ ? 'mul'
#         f l.... x,y ? * ?
#     ____ ? 'sub'
#         f l.... x,y ? - ?
#     ____ ? 'add'
#         f l.... x,y ? + ?
#     ____ ? 'div'
#         f l.... x,y ? / ?
#
#
#     ___
#         res ? ? n..
#     ______ Z..
#         ? 0
#
#
#     __ stdout
#         print ?
#
#     r.. ?
#
#
#
# __ _____ __ _____
#     ? s.._T..
