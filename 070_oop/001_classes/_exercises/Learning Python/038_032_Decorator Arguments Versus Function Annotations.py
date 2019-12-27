# # Using decorator arguments
# 
# ___ rangetest 00 argchecks
#     ___ onDecorator func
#         ___ onCall *pargs **kargs
#             print argch..
#             ___ check i_ a... p..     # Add validation code here
#             r_ fu.. *pargs **kargs
#         r_ o..
#     r_ on...
# 
# _r.. (a_(1, 5), c_(0.0, 1.0))
# ___ func a, b, c                           # func = rangetest(..)(func)
#     print(a + b + c)
# 
# f.. (1, 2, c=3)                              # Runs onCall, argchecks in scope
# 
# 
# # Using function annotations
# 
# ___ rangetest func
#     ___ onCall *pargs **kargs
#         argchecks _ f__. -a
#         print ?
#         ___ check i_ ? p..         # Add validation code here
#         r_ f.. 0pa.. 00ka..
#     r_ o..
# 
# _r..
# ___ func(a:(1, 5), b, c:(0.0, 1.0)):         # func = rangetest(func)
#     print(a + b + c)
# 
# func(1, 2, c=3)                              # Runs onCall, annotations on func
# 
