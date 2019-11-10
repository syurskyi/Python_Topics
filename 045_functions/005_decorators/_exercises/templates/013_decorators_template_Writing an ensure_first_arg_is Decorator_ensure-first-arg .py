# # ######################################################################################################################
# 290. Writing an ensure_first_arg_is Decorator_ensure-first-arg

# f_ f_ i_ w_
#
# ___ ensure_first_arg_is val
#     ___ inner fn
#         _wraps fn
#         ___ wrapper _args __kwargs
#             __ args a_ args|0| |- val
#                 r_ _ First arg needs to be |val|
#             r_ fn _args __kwargs
#         r_ wra___
#     r_ inn__
#
# _ensure_first_arg_is _burrito_
# ___ fav_foods _foods
#     print foods
#
# print fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
# print fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'
#
# _ensure_first_arg_is 10
# ___ add_to_ten num1 num2
#     r_ num1 + num2
#
# print(add_to_ten(10, 12))  # 12
# print(add_to_ten(1, 2))  # 'Invalid! First argument must be 10'
#
# print()