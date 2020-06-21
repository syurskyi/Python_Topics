# """Template method pattern
#
# Template Method is a behavioral design pattern. It defines an algorithm's
# skeleton in a Base c_, but lets subclasses redefine certain steps of the
# algorithm. The Base c_ declares some placeholder methods, and derived classes
# implement them.
# """
# ______ ___
# ____ a.. ______ A.. a..
#
#
# c_ Algorithm A..
#
#     ___ template_method
#         """Skeleton of operations to perform. DON'T override me.
#
#         The Template Method defines a skeleton of an algorithm in an operation,
#         and defers some steps to subclasses.
#         """
#         ?
#         ?
#         ?
#         ?
#
#     ___ __do_absolutely_this
#         """Protected operation. DON'T override me."""
#         this_method_name _ ___._g_f__.f_c__.c_n..
#         print("@.@".f..  -c . -n  ?
#
#     ??
#     ___ do_step_1
#         """Primitive operation. You HAVE TO override me, I'm a placeholder."""
#         pass
#
#     ??
#     ___ do_step_2
#         """Primitive operation. You HAVE TO override me, I'm a placeholder."""
#         pass
#
#     ___ do_something
#         """Hook. You CAN override me, I'm NOT a placeholder."""
#         print("do something")
#
#
# c_ AlgorithmA A..
#
#     ___ do_step_1
#         print("do step 1 for Algorithm A")
#
#     ___ do_step_2
#         print("do step 2 for Algorithm A")
#
#
# c_ AlgorithmB A..
#
#     ___ do_step_1
#         print("do step 1 for Algorithm B")
#
#     ___ do_step_2
#         print("do step 2 for Algorithm B")
#
#     ___ do_something
#         print("do something else")
#
#
# ___ main
#     print("Algorithm A")
#     a _ AA
#     ?.t_m..
#
#     print("\nAlgorithm B")
#     b _ AB
#     ?.t_m..
#
#
# __ ________ __ _________
#     ?
