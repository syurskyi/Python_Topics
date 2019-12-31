# _____ __
#
#
# ___ create_module_file module_name $$
#     '''Create a module file named <module_name>.py.
#     Module has a single function (print_values) that will print
#     out the supplied (stringified) kwargs.
#     '''
#
#     module_file_name = _ |m__ .py
#     module_rel_file_path = ?
#     module_abs_file_path = __.pa__.a.. ?
#
#     w___ o.. m_a.. _ __ f:
#         ?.w.. _*# |module_name| .py\n\n
#         ?.w.. _*print('running |m_f_n.. ...')\n\n")
#         ?.w.. _*def print_values():\n')
#         ___ key value __ k___.it..
#             ?.w.. _ *\tprint('|st_ k..', '|st. v.. ')\n")
#
# create_module_file('test', k1_10, k2_'python')
#
# _____ test
#
# print(test)
# print(test.print_values())
#
# ###########################################################################
# print('#' * 52 + ' change test module')
#
# ? 'test', k1_10 k2_'python' k3_'cheese'
# print(test.print_values())
#
# ###########################################################################
# print('#' * 52 + ' import module again')
#
# _____ test
# print(test.print_values())
#
# print(id(test))
#
# _____ ___
# del ___.m.. t..
#
# ###########################################################################
# print('#' * 52 + ' import module again')
#
# _____ test
#
# print(test.print_values())
#
# print(id(test))
# print(id(test))
#
# ###########################################################################
# print('#' * 52 + ' create module file')
#
# ? 'test' k1_10 k2_ python
#                    k3_ cheese k4_ parrots
#
# _____ __l___
# print(__l___.r... t..
# print(id(test))
#
# print(test.print_values())
#
# ? test2 k1_python
#
# ###########################################################################
# print('#' * 52 + ' from test2 import module again')
#
# ____ test2 _____ print_values
#
# print_values()
#
# print(id(print_values()))
#
# ? test2 k1_ python k2_cheese
#
# # importlib.reload(test2)
#
# # ---------------------------------------------------------------------------
# # NameError                                 Traceback (most recent call last)
# # <ipython-input-26-7b4c6fe87427> in <module>()
# # ----> 1 importlib.reload(test2)
# #
# # NameError: name 'test2' is not defined
#
#
# ###########################################################################
# print('#' * 52 + ' import test2')
#
# _____ test2
#
# print(test2.print_values())
# print(id(test2.print_values))
# print(id(print_values))
#
# print(__l___.reload(test2))
# print(test2.print_values())
# print(print_values())
# print(id(test2.print_values))
# print(id(print_values))