#  Decorators With Different Signatures
# shout example

# ___ shout fn
#     ___ wrapper _args __kwargs
#         r_ fn _args __kwargs.u_
#     r_ wr__
#
# _shout
# ___ greet name
#     r_ f"Hi, I'm |name|."
#
# _shout
# ___ order main side
#     r_ _"Hi, I'd like the |main|, with a side of |side|, please."
#
# _shout
# ___ lol
#     r_ "lol"
#
# print greet("todd")
# print(order(side_"burger" main_"fries"))
# print(lol())
#
# print()