# c_ tracer:
#     ___ - ____, func):                # On @ decorator
#         ____.calls _ 0                       # Save func for later call
#         ____.f..  _ f..
#     ___ -c ____, $ $$:     # On call to original function
#         ____.c... +_ 1
#         print('call @ to @' @ ____.c... ____.f___. -n
#         r_ ____.func($ $$
#
#
# _t..
# ___ spam(a, b, c):                           # spam = tracer(spam)
#     print(a + b + c)                         # Triggers tracer.__init__
#
# spam(1, 2, 3)                                # Runs tracer.__call__
# spam(a=4, b=5, c=6)                          # spam is an instance attribute
#
# c_ Person
#     ___ - ____ name pay
#         ____.n.. _ n..
#         ____.p..  _ p..
#
#     _t..
#     ___ giveRaise ____ percent            # giveRaise = tracer(giverRaise)
#         ____.pay *_ (1.0 + p...
#
#     _t..
#     ___ lastName ____                      # lastName = tracer(lastName)
#         r_ ____.n___.sp.. -1
#
# bob _ ? Bob Smith 50000             # tracer remembers method funcs
# # bob.giveRaise(.25)                           # Runs tracer.__call__(???, .25)
# # print(bob.lastName())                        # Runs tracer.__call__(???)
#
