# ____ fun.. ______ w..
# ______ l..
#
# ___ logged level name_N.. message_N..
#     '''
#     Add logging to a function.  level is the logging
#     level, name is the logger name, and message is the
#     log message.  If name and message aren't specified,
#     they default to the function's module and name.
#     '''
#     ___ decorate func
#         logname _ name __ ? ____ ?. -m
#         log _ l___.gL.. ?
#         logmsg _ m.. __ m.. ____ ?. -n
#
#         ?w.. ?
#         ___ wrapper $ ##
#             l__.l.. l.. l_m..
#             r_ ? $ $$
#         r_ ?
#     r_ ?
#
# # Example use
# ?l.. l__.D..
# ___ add x y
#     r_ ? + ?
#
# ?l.. l___.C.. *example
# ___ spam(
#     print('Spam!')
#
# __ _______ __ ______
#     ______ l..
#     l___.bC.. l_l__.D..
#     print ? 2,3
#     spam()
#
# # Problem
# # You want to write a decorator function that takes arguments.
# # Solution
# # Let’s illustrate the process of accepting arguments with an example. Suppose you want
# # to write a decorator that adds logging to a function, but allows the user to specify the
# # logging level and other details as arguments. Here is how you might define the decorator:
#
# # On first glance, the implementation looks tricky, but the idea is relatively simple. The
# # outermost function logged() accepts the desired arguments and simply makes them
# # available to the inner functions of the decorator. The inner function decorate() accepts
# # a function and puts a wrapper around it as normal. The key part is that the wrapper is
# # allowed to use the arguments passed to logged().
# # Discussion
# # Writing a decorator that takes arguments is tricky because of the underlying calling
# # sequence involved. Specifically, if you have code like this:
#
# # The decoration process evaluates as follows:
# # ___ func(a, b):
# # pass
# # func _ decorator(x, y, z)(func)
# # Carefully observe that the result of decorator(x, y, z) must be a callable which, in
# # turn, takes a function as input and wraps it. See Recipe 9.7 for another example of a
# # decorator taking arguments.