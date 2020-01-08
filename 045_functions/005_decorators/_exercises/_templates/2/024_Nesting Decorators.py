# ____ fun__
#
# ___ debug func
#     """Print the function signature and return value"""
#     ??.? ?
#     ___ wrapper_debug $ $$
#         args_repr _ |repr|a| ___ a __ a__|                      # 1
#         kwargs_repr _ |_*|k|=|v!r|* ___ k, v __ k__.i__  # 2
#         signature _ *, *.j___|a00_r00 + k00_r0|          # 3
#         print _*Calling ?. -n|||s...||*|
#         value _ ? $ $$
#         print _*|?. -n!r| returned |va..!r|*|           # 4
#         r_ ?
#     r_ ?
#
# ___ do_twice func
#     ??.? ?
#     ___ wrapper_do_twice $ $$
#         ? $ $$
#         r_ f00 $ $$
#     r_ ?
#
#
# ?d__
# ?do_
# ___ greet name
#     print _*Hello |name
#
# ? Eva
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
# ? Eva
# # Calling greet('Eva')
# # Hello Eva
# # 'greet' returned None
# # Calling greet('Eva')
# # Hello Eva
# # 'greet' returned None
#
