# # def do_twice(func):
# #     def wrapper_do_twice():
# #         func()
# #         func()
# #     return wrapper_do_twice
#
# ___ do_twice func
#     ___ wrapper_do_twice $ $$
#         ? $ $$
#         ? $ $$
#     r_ ?
#
# ??
# ___ return_greeting name
#     print Creating greeting
#     r_ _ Hi |name       # new formating
#
# hi_adam _ ? Adam
# # Creating greeting
# # Creating greeting
# print ?
# # None
#
# # Oops, your decorator ate the return value from the function.
# #
# # Because the do_twice_wrapper() doesn’t explicitly return a value, the call return_greeting("Adam")
# # ended up returning None.
# #
# # To fix this, you need to make sure the wrapper function returns the return value of the decorated function.
#
# ___ do_twice func
#     ___ wrapper_do_twice $ $$
#         ? $ $$
#         r_ $ $$ $ $$
#     r_ ?
#
# $
# ___ return_greeting name
#     print Creating greeting
#     r_ _ Hi |name             # new formating
#
# hi_adam _ ? Adam
#
# re... Adam
# # Creating greeting
# # Creating greeting
# # 'Hi Adam'