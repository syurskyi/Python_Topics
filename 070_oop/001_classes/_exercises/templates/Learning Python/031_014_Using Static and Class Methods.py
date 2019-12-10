# # A decorator for both functions and methods
#
# ___ tracer func                        # Use function, not class with __call__
#     calls = 0                            # Else "self" is decorator instance only!
#     ___ onCall($ $$:
#         no... ?
#         ? +_ 1
#         print('call @ to @' @ c.. func. -n
#         r_ f.. $ $$
#     r_ o...
#
#
# # Applies to simple functions
#
# _t...
# ___ spam(a, b, c):                       # spam = tracer(spam)
#     print(a + b + c)                     # onCall remembers spam
#
# spam(1, 2, 3)                            # Runs onCall(1, 2, 3)
# spam(a=4, b=5, c=6)
#
#
# # Applies to class method functions too!
#
# c_ Person
#     ___ - ___ name pay
#         ___.n... _ n...
#         ___.p..  _ p..
#
#     _t...
#     ___ giveRaise ___ percent        # giveRaise = tracer(giverRaise)
#         ___.p.. *_ (1.0 + p...      # onCall remembers giveRaise
#
#     _t...
#     ___ lastName ___                  # lastName = tracer(lastName)
#         r_ ___.n....sp.. -1
#
# print('methods...')
# bob = Person('Bob Smith', 50000)
# sue = Person('Sue Jones', 100000)
# print(bob.n..., sue.n...)
# sue.giveRaise(.10)                       # Runs onCall(sue, .10)
# print(sue.p..)
# print(bob.lastName(), sue.lastName())    # Runs onCall(bob), lastName in scopes
