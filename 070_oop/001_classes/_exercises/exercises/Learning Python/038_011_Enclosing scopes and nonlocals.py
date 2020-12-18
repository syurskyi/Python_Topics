# ___ tracer func                        # State via enclosing scope and nonlocal
#     calls = 0                            # Instead of class attrs or global
#     ___ wrapper $ $$        # calls is per-function, not global
#         no... ?
#         ? += 1
#         print('call @ to @' @ c.. f___. -n
#         r_ f.. $ $$
#     r_ w..
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
# eggs(4, y=4)              # Nonlocal calls _is_ not per-function here
