# c_ Descriptor o...
#     ___ -g  ____ instance owner  ...
#
# c_ Subject:
#     attr = D...
#
# X = S..
# ?.a..         # Roughly runs Descriptor.__get__(Subject.attr, X, Subject)
#
#
# c_ tracer o...
#     ___ -  ____ func                # On @ decorator
#         ____.calls _ 0                       # Save func for later call
#         ____.f..  _ f..
#
#     ___ -c ____ $  $$     # On call to original func
#         ____.calls += 1
#         print('call @ to @' @ ____.c.. ____.f___. -n
#         r_ ____.func($  $$
#
#     ___ -g ____ instance owner      # On method attribute fetch
#         r_ w... ____ in..
#
#
# c_ wrapper
#     ___ - ____ desc subj         # Save both instances
#         ____.d.. _ d..                     # Route calls back to  decr
#         ____.s... _ s..
#
#     ___ -c ____ $  $$
#         r_ ____.d___ ____.s... $  $$  # Runs tracer.__call__
#
# _t..
# ___ spam(a, b, c):                           # spam = tracer(spam)
#     p...                                    # Uses __call__ only
#
#
# c_ Person
#     _t..
#     ___ giveRaise ____ percent            # giveRaise = tracer(giverRaise)
#         p..                                 # Makes giveRaise a descriptor
#
#
# c_ tracer(o...
#     ___ - ____ func                # On @ decorator
#         ____.calls _ 0                       # Save func for later call
#         ____.f...  _ f...
#
#     ___ -c ____ $  $$:     # On call to original func
#         ____.calls += 1
#         print('call @ to @' @ (____.c.. ____.f___. -n
#         r_ ____.f__ $  $$
#
#     ___ -g ____ instance owner                # On method fetch
#         ___ wrapper $  $$                  # Retain both inst
#             r_ ____ in.. $  $$     # Runs __call__
#         r_ w...
#
