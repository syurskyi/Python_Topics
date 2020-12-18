# c_ Callee
#     ___ -c ____ $p $$k   # Intercept instance calls
#         print('Called:', pa.. ka..     # Accept arbitrary arguments
#
# C = ?
# print('#' * 23 + ' C is a callable object')
# C(1, 2, 3)                                 # C is a callable object
# C(1, 2, 3, x=4, y=5)
#
# # class C:
# #     def __call__(____, a, b, c=5, d=6):       # Normals and defaults
# #
# # # class C:
# #     # def __call__(____, *pargs, **kargs):      # Collect arbitrary arguments
# #
# # class C:
# #     def __call__(____, d=6, *pargs, **kargs):   # 3.0 keyword-only argument
# #
# X = ?
# print('#' * 23 + ' Omit defaults')
# X(1, 2)                             # Omit defaults
# print('#' * 23 + '  Positionals')
# X(1, 2, 3, 4)                       # Positionals
# print('#' * 23 + ' Keywords')
# X(a=1, b=2, d=4)                    # Keywords
# print('#' * 23 + ' Unpack arbitrary arguments')
# X(*[1, 2], **dict(c=3, d=4))        # Unpack arbitrary arguments
# print('#' * 23 + ' Mixed modes')
# X(1, *(2,), c=3, **dict(d=4))       # Mixed modes
#
# #
# c_ Prod
#     ___ - ____ value            # Accept just one argument
#         ____.?  ?
#
#     ___ -c ____ other
#         r_ ____.v.. * o..
#
# x = ? 2                                # "Remembers" 2 in state
# print('#' * 23 + ' "Remembers" 2 in state')
# print(x(3))                                       # 3 (passed) * 2 (state)
# print('#' * 23 + ' "3 (passed) * 2 (state)')
# print(x(4))
#
#
# c_ Prod
#     ___ - ____ value
#         ____.?  ?
#     ___ comp ____ other
#         r_ ____.v.. * o..
#
# x = ? 3
# print('#' * 23)
# print(?.c.. 3
# #
# print(?.c.. 4
# #
# #
# #
# #
# c_ Callback
#     ___ - ____ color             # Function + state information
#         ____.?  ?
#
#     ___ -c ____                      # Support calls with no arguments
#         print('turn', ____.?
#
#
# # cb1 = ? blue                      # Remember blue
# # cb2 = ? green
# #
# # B1 = Button(command=cb1)                     # Register handlers
# # B2 = Button(command=cb2)                     # Register handlers
# #
# #
# # cb1()                                        # On events: prints 'blue'
# # cb2()                                        # Prints 'green'
# #
# #
# #
# # cb3 = (lambda color='red': 'turn ' + color)  # Or: defaults
# # print(cb3())
# #
# #
# #
# # class Callback:
# #     def __init__(____, color):               # Class with state information
# #         ____.color = color
# #     def changeColor(____):                   # A normal named method
# #         print('turn', ____.color)
# #
# # cb1 = Callback('blue')
# # cb2 = Callback('yellow')
# #
# # B1 = Button(command=cb1.changeColor)         # Reference, but don't call
# # B2 = Button(command=cb2.changeColor)         # Remembers function+____
# #
# #
# #
# # object = Callback('blue')
# # cb = object.changeColor                      # Registered event handler
# # cb()                                         # On event prints 'blue'
