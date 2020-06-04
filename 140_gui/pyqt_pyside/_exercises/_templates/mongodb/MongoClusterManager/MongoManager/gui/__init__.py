# ___ _import_all_modules
#     """dynamically imports all modules in the package"""
#     ______ t__
#     ______ __
#     g__ -a
#     -a _   # list
#     globals_ locals_ _ g.. l..
#
#     # dynamically import all the package modules
#     ___ filename __ __.l.. -n
#         # process all python files in directory that don't start with underscore
#         # (which also keeps this module from importing itself)
#         __ ? 0 !_ '_' an. ?.s.. '.' -1 __ 'py' 'pyw'
#             modulename _ ?.s.. '.' 0  # filename without extension
#             package_module _ '.'.j.. -n.. ?
#             ___
#                 module _ -i p.. g.._ l.._ |m..
#             ______
#                 t__.p_e..
#                 r_
#             ___ name __ m__.-d
#                 __ no. ?.s_w_ '_'
#                     g.._|n.. _ m...-d |?
#                     -a.ap.. ?
#
#
# ?
