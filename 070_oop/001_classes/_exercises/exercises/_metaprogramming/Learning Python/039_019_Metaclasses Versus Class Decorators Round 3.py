# # Class decorator factory: apply any decorator to all methods of a class
# 
# f__ ty.. ______ F..T..
# f__ mytools2 ______ tracer, timer
# 
# ___ decorateAll decorator
#     ___ DecoDecorate aClass
#         ___ attr, attrval i_ a__. -d .it..
#             i_ ty.. a.. i_ F.T.
#                 s... aC.. a.. d.. a..        # Not __dict__
#         r_ a..
#     r_ D..
# 
# _d.. t..                          # Use a class decorator
# c_ Person                                 # Applies func decorator to methods
#     ___ - ____ name pay            # Person = decorateAll(..)(Person)
#         ____.n.. _ n..                      # Person = DecoDecorate(Person)
#         ____.p..  _ p..
#     ___ giveRaise ____ percent
#         ____.pay *_ (1.0 + p..
#     ___ lastName ____
#         r_ ____.n__.s.. -1
# 
# bob = ?('Bob Smith', 50000)
# sue = ?('Sue Jones', 100000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())
# 
# # @decorateAll(tracer)                 # Decorate all with tracer
# 
# # @decorateAll(timer())                # Decorate all with timer, defaults
# 
# # @decorateAll(timer(label='@@'))      # Same but pass a decorator argument
# 
# # If using timer: total time per method
# 
# print('-' * 40)
# print('@.5_' @ P__. - .a..
# print('@.5_' @ P__.g.R_.a.
# print('@.5_' @ P__.l.N_.a..
