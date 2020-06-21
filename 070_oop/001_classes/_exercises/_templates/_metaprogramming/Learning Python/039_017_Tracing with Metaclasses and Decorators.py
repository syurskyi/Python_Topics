# # Metaclass that adds tracing decorator to every method of a client class
# 
# f__ ty.. ________ F..T..
# from mytools2 import tracer
# 
# c_ MetaTrace ty..
#     ___  - meta classname supers classdict
#         ___ attr, attrval i_ cl.d_.it..
#             i_ ty.. attr... i_ F.T.                      # Method?
#                 c.d. a.. _ t... attr..                  # Decorate it
#         r_ ty_. -n m.. c... s... cl..    # Make class
# 
# c_ Person m.. _ M..
#     ___ - ____ name pay
#         ____.n.. _ n..
#         ____.p..  _ p..
#     ___ giveRaise ____ percent
#         ____.pay *= (1.0 + p..
#     ___ lastName ____
#         r_ ____.n__.sp.. -1
# 
# bob = ?('Bob Smith', 50000)
# sue = ?('Sue Jones', 100000)
# print(bob.name, sue.name)
# sue.giveRaise(.10)
# print(sue.pay)
# print(bob.lastName(), sue.lastName())
# 
