#  Decorators With Different Signatures
# shout example

# ___ shout fn
#     ___ wrapper _args __kwargs
#         r_ fn _a... __k____|.u_
#     r_ wr__
#
# _s....
# ___ greet name
#     r_ f"Hi, I'm |n..|."
#
# _s....
# ___ order main side
#     r_ _"Hi, I'd like the |m..|, with a side of |s..|, please."
#
# _s...
# ___ lol
#     r_ "lol"
#
# print greet("todd")
# print(order(side_"burger" main_"fries"))
# print(lol())
#
# print()