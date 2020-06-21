# c_ Property:
#     ___ -  ____, fg.. _ N.. fs.. _ N.. fd.. _ N.. do. _ N..
#         ____.fg.. _ fg..
#         ____.fs.. _ fs..
#         ____.fd.. _ fd..                                  # Save unbound methods
#         ____. -d _ do.                                # or other callables
#
#     ___ -g ____ instance instancetype _ N..
#         i_ instance i_ N...
#             r_ ____
#         i_ ____.fget i_ N...
#             r.... A...("can't get attribute")
#         r_ ____.fg.. ins...                        # Pass instance to ____
#                                                           # in property accessors
#     ___ -s ____ instance value
#         i_ ____.fs.. i_ N...
#             r.... A...("can't set attribute")
#         ____.fs.. i... v...
#
#     ___ __delete__ ____ instance
#         i_ ____.fd.. i_ N...
#             r.... A...("can't delete attribute")
#         ____.fd.. i...
#
# c_ Person
#     ___ getName ____ ...
#     ___ setName ____ value ...
#     name _ P... g.. s...                     # Use like property()
#
