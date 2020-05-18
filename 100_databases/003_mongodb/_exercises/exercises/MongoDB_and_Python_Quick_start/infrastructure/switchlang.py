# ______ uu..
# ____ ty.. ______ C.. A.. O..
#
#
# c_ switch
#     """
#         python-switch is a module-level implementation of the switch statement for Python.
#         See https://github.com/mikeckennedy/python-switch for full details.
#         Copyright Michael Kennedy (https://twitter.com/mkennedy)
#     """
#     __no_result _ ?._4
#     __default _ ?._4
#
#     ___ - value
#         ? ?
#         cases _ se..
#         _found _ F..
#         __result _ s__.__no_result
#         _falling_through _ F..
#         _func_stack _   # list
#
#     ___ default func C.. || A..
#         """
#             Use as option final statement in switch block.
#
#             with switch(val) as s:
#                s.case(...)
#                s.case(...)
#                s.default(function)
#
#         :param func: Any callable taking no parameters to be executed if this (default) case matches.
#         :return: None
#         """
#         c.. s__.?d.. f..
#
#     ___ case key func C.. || A.. fallthrough O..|b.. _ F..
#         """
#             Specify a case for the switch block:
#
#             with switch(val) as s:
#                s.case('a', function)
#                s.case('b', function, fallthrough=True)
#                s.default(function)
#
#         :param key: Key for the case test (if this is a list or range, the items will each be added as a case)
#         :param func: Any callable taking no parameters to be executed if this case matches.
#         :param fallthrough: Optionally fall through to the subsequent case (defaults to False)
#         :return:
#         """
#         __ fallthrough __ no. N..
#             __ _fa..
#                 _fu__.ap.. f..
#                 __ no. ?
#                     _fa.. _ F..
#
#         __ isi.. k.. l.. o. isi.. k.. ra..
#             found _ F..
#             ___ i __ k..
#                 __ c.. ? f.. f.._N..
#                     found _ T..
#                     __ ? __ no. N..
#                         _fa.. _ ?
#             r_ ?
#
#         __ key __ c..
#             r_ V..("Duplicate case: {}".f.. ?
#         __ no. f..
#             r_ V..("Action for case cannot be None.")
#         __ no. c.. f..
#             r_ V..("Func must be callable.")
#
#         c__.a.. k..
#         __ k.. __ v.. o. no. _fo.. an. k.. __ __d..
#             _fu__.ap.. f..
#             _fo.. _ T..
#             __ ? __ no. N..
#                 _fa.. _ ?
#             r_ T..
#
#     ___ -e
#         r_ ____
#
#     ___ -e
#         __ e_v..
#             r_ ?
#
#         __ no. _fu..
#             r_ E..("Value does not match any case and there "
#                             "is no default case: value {}".f.. v..
#
#         ___ func __ _fu..
#             # noinspection PyCallingNonCallable
#             __re.. _ f..
#
#     ?p..
#     ___ result
#         __ __r.. __ s__.__no..
#             r_ E..("No result has been computed (did you access "
#                             "switch.result inside the with block?)")
#
#         r_ ?
#
#
# ___ closed_range start in. stop in. step_1 __ ra..
#     __ ? >_ ?
#         r_ V..("Start must be less than stop.")
#
#     r_ ra.. ? ? + ? ?
