# import functools
#
# ___ debug func
#     """Print the function signature and return value"""
#     _f00.w00 f00
#     ___ wrapper_debug _a__ __kwargs
#         args_repr _ |repr|a| ___ a i_ a___|                      # 1
#         kwargs_repr _ |_*|k|_|v!r|* ___ k_ v i_ k___.i__|||  # 2
#         signature + *, *.jo00|a00_r00 + k00_r00|           # 3
#         print _*Calling |f0.__n__|||signature||*|
#         value _ f00 _a__ __k__
#         print _*|f00.__n__!r| returned |value!r|*|           # 4
#         r_ v00
#     r_ w00
#
# _d00
# ___ make_greeting name age_N____
#     i_ age i_ N__
#         r_ _*Howdy |name|!*
#     e___
#         r_ _*Whoa |name|! |age| already, you are growing up!*
#
# make_greeting Benjamin
# # Calling make_greeting('Benjamin')
# # 'make_greeting' returned 'Howdy Benjamin!'
# # 'Howdy Benjamin!'
#
# make_greeting Richard age_112
# # Calling make_greeting('Richard', age=112)
# # 'make_greeting' returned 'Whoa Richard! 112 already, you are growing up!'
# # 'Whoa Richard! 112 already, you are growing up!'
#
# make_greeting name_ Dorrisile age_116
# # Calling make_greeting(name='Dorrisile', age=116)
# # 'make_greeting' returned 'Whoa Dorrisile! 116 already, you are growing up!'
# # 'Whoa Dorrisile! 116 already, you are growing up!'
#
