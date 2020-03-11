# ____ a.. _______ a..
#
#
# c_ Machine:
#     ___ print document
#         r_ N...
#
#     ___ fax document
#         r_ N...
#
#     ___ scan document
#         r_ N...
#
#
# # ok if you need a multifunction device
# c_ MultiFunctionPrinter M..
#     ___ print document
#         p..
#
#     ___ fax document
#         p..
#
#     ___ scan document
#         p..
#
#
# c_ OldFashionedPrinter(M..
#     ___ print document
#         # ok - print stuff
#         p..
#
#     ___ fax document
#         p..  # do-nothing
#
#     ___ scan document
#         """Not supported!"""
#         r_ N...('Printer cannot scan!')
#
#
# c_ Printer
#     ?a..
#     ___ print document p..
#
#
# c_ Scanner:
#     ?a..
#     ___ scan document p..
#
#
# # same for Fax, etc.
#
# c_ MyPrinter Printer
#     ___ print document
#         print ?
#
#
# c_ Photocopier P.. S..
#     ___ print document
#         print ?
#
#     ___ scan document
#         p..  # something meaningful
#
#
# c_ MultiFunctionDevice P.. S..  # , Fax, etc
#     ?a..
#     ___ print document
#         p..
#
#     ?a..
#     ___ scan document
#         p..
#
#
# c_ MultiFunctionMachine M..
#     ___ - printer scanner
#         ??  ?
#         ??  ?
#
#     ___ print document
#         p__.p.. ?
#
#     ___ scan document
#         s__.s.. ?
#
#
# printer = OldFashionedPrinter()
# printer.fax(123)  # nothing happens
# printer.scan(123)  # oops!
