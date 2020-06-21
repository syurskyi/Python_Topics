# # -*- coding: utf-8 -*-
# ____ f... ______ s...
#
#
# ?s..
# ___ add a b
#     r... No...  Unsupported type
#
#
# ?a__.r.. in.
# ___ _ a b     # _ original
#     print("First argument is of type " ty.. a
#     print(a + b)
#
#
# ??.r_. st.
# ___ _ a b           # _ original
#     print("First argument is of type " ty.. a
#     print(a + b)
#
#
# ??.r.. li..
# ___ _ a b          # _ original
#     print("First argument is of type ", ty.. a
#     print(a + b)
#
#
# __ ______ __ ______
#     add(1, 2)
#     add('Python', 'Programming')
#     add([1, 2, 3], [5, 6, 7])
#
# # First argument is of type <class 'int'>
# # 3
# #
# # First argument is of type <class 'str'>
# # PythonProgramming
# #
# # First argument is of type <class 'list'>
# # [1, 2, 3, 5, 6, 7]
# #
# # Traceback (most recent call last):
# #     File "overloads.py", line 30, in <module>
# #         add({}, 1)
# #     File "/usr/local/lib/python3.5/functools.py", line 743, in wrapper
# #         return dispatch(args[0].__class__)(*args, **kw)
# #     File "overloads.py", line 5, in add
# #         raise NotImplementedError('Unsupported type')
# # NotImplementedError: Unsupported type
