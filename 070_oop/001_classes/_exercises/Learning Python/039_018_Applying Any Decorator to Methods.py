# 
# # Metaclass factory: apply any decorator to all methods of a class
# 
# f___ ty.. _______ F.T.
# from mytools2 import tracer, timer
# 
# ___ decorateAll decorator
#     c_ MetaDecorate ty..
#         ___ -n meta classname supers classdict
#             ___ attr, attrval i_ cl__.it..
#                 __ ty.. at.. i_ F..T.
#                     cl.. a.. _ decorator att..
#             r_ ty__. -n m... c... s.. cl..
#     r_ MetaDecorate
# 
# c_ Person m.. _ d.. tr..       # Apply a decorator to all
#     ___ - ____ name pay
#         ____.n.. _ n..
#         ____.p..  _ p..
#     ___ giveRaise ____ percent
#         ____.pay *= (1.0 + percent)
#     ___ lastName ____
#         r_ ____.na__.sp.. -1
# 
# bob = P_('Bob Smith', 50000)
# sue = P_('Sue Jones', 100000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())
# 
# c_ ?(m.. _ d... tr..               # Apply tracer
# 
# c_ ?(m.. _ d.. ti..              # Apply timer, defaults
# 
# c_ ?(m.. = d.. ti.. label_'**'    # Decorator arguments
# 
# 
# 
# # If using timer: total time per method
# 
# print('-'*40)
# print('@.5_' @ P__. - .a...
# print('@.5_' @ P__.g_R_.a...
# print('@.5_' @ P__.l_N_.a...
