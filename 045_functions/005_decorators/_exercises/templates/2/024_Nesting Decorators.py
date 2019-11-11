# ____ fun__
#
# ___ debug func
#     """Print the function signature and return value"""
#     _f00.w00 f00
#     ___ wrapper_debug 0args 00k__
#         args_repr _ |repr|a| ___ a i_ a__|                      # 1
#         kwargs_repr _ |_*|k|=|v!r|* ___ k, v i_ k00.i00|||  # 2
#         signature _ *, *.j___|a00_r00 + k00_r0|           # 3
#         print _*Calling |f00.__n__|||signature||*|
#         value _ f00 0a___ 00k__
#         print _*|f00.__n__!r| returned |value!r|*|           # 4
#         r_ v00
#     r_ w00
#
# ___ do_twice func
#     0fun.w000 f000
#     ___ wrapper_do_twice 0a__ 00k__
#         f00 0a__ 00k__
#         r_ f00 0a__ 00k__
#     r_ w00
#
#
# 0d__
# 0do_00
# ___ greet name
#     print _*Hello |name|
#
# greet Eva
# # Calling greet('Eva')
# # Hello Eva
# # Hello Eva
# # 'greet' returned None
#
# # observe the difference if we change the order of @debug and @do_twice:
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
# print('#' * 52 + '  ')
#
# greet Eva
# # Calling greet('Eva')
# # Hello Eva
# # 'greet' returned None
# # Calling greet('Eva')
# # Hello Eva
# # 'greet' returned None
#
