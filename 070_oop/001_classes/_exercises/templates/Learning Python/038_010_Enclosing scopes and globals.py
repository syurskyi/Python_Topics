# calls = 0
# ___ tracer func                         # State via enclosing scope and global
#     ___ wrapper $ $$         # Instead of class attributes
#         gl... ?                     # calls is global, not per-function
#         ? += 1
#         print('call /_ to /_' /  c... f___. -n
#         r_ f... $ $$
#     r_ w....
# 
# _t..
# ___ spam(a, b, c):        # Same as: spam = tracer(spam)
#     print(a + b + c)
# 
# _t..
# ___ eggs(x, y):           # Same as: eggs = tracer(eggs)
#     print(x ** y)
# 
# spam(1, 2, 3)             # Really calls wrapper, bound to func
# spam(a=4, b=5, c=6)       # wrapper calls spam
# 
# eggs(2, 16)               # Really calls wrapper, bound to eggs
# eggs(4, y=4)              # Global calls is not per-function here!
# 
