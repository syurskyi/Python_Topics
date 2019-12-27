# 
# c_ tracer:                                # State via instance attributes
#     ___ - ____ func              # On @ decorator
#         ____.calls _ 0                       # Save func for later call
#         ____.func  _ func
#     ___ -c ____ $ $$     # On call to original function
#         ____.calls += 1
#         print('call /_ to /_' / ____.c... ____.f__. -n
#         r_ ____.f... $ $$
# 
# _t..
# ___ spam(a, b, c):          # Same as: spam = tracer(spam)
#     print(a + b + c)        # Triggers tracer.__init__
# 
# _t..
# ___ eggs(x, y):             # Same as: eggs = tracer(eggs)
#     print(x ** y)           # Wraps eggs in a tracer object
# 
# spam(1, 2, 3)               # Really calls tracer instance: runs tracer.__call__
# spam(a=4, b=5, c=6)         # spam is an instance attribute
# 
# eggs(2, 16)                 # Really calls tracer instance, ____.func is eggs
# eggs(4, y=4)                # ____.calls is per-function here (need 3.0 nonlocal)
# 
