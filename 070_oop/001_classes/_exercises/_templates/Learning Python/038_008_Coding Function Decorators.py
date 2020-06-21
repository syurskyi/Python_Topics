# ### file: decorator1.py
#
# c_ tracer:
#     ___ - ____, func):             # On @ decoration: save original func
#         ____.calls _ 0
#         ____.func _ f...
#     ___ -c ____ $           # On later calls: run original func
#         ____.c.. +_ 1
#         print('call /_ to /_' /  ____.c.... ____.f___. -n
#         ____.f... $
#
# _t...
# ___ spam(a, b, c)           # spam = tracer(spam)
#     print(a + b + c)         # Wraps spam in a decorator object
#
# # from decorator1 import spam
#
# print('#' * 23 + ' Really calls the tracer wrapper object')
# spam(1, 2, 3)            # Really calls the tracer wrapper object
# # call 1 to spam
# # 6
# #
#
# print('#' * 23 + ' Invokes __call__ in class')
# spam('a', 'b', 'c')      # Invokes __call__ in class
# # call 2 to spam
# # abc
# #
# print('#' * 23 + ' Number calls in wrapper state information')
# print(spam.calls)               # Number calls in wrapper state information
# # 2
# print(spam)
# # <decorator1.tracer object at 0x02D9A730>
# #
#
# calls _ 0
# ___ tracer func, $
#     gl... ?
#     ? +_ 1
#     print('call /_ to /_' / c.. f__. -n
#     f.. $
# #
# ___ spam(a, b, c):
#     print(a, b, c)
# #
#
# print('#' * 23 + ' Normal non-traced call: accidental?')
# spam(1, 2, 3)            # Normal non-traced call: accidental?
# # 1 2 3
# #
# print('#' * 23 + ' Special traced call without decorators')
# tracer(spam, 1, 2, 3)    # Special traced call without decorators
# # call 1 to spam
# # 1 2 3
