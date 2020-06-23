# # -*- coding: utf-8 -*-
#
# # how many times each character occurred in a string:
# text _ 'Some long text'
# counts _ di__
# ___ c __ ?
#     key _ ?.lo..  .st..
#     __ ?
#         ?|?| _ co__.ge. ke., 0  + 1
# print co___
#
# # how many times each character occurred in a string:
# #
# # Suppose now that we just want a dictionary to track the uppercase, lowercase, and other characters i_ the st___
# #  i.e. kind of grouping the data by uppercase, lowercase, other  - again ignoring spaces:
# ______ st___
#
# print st___.a.._l..
# print st___.a.._u..
#
# text _ 'Some long text'
#
# categories _  # dict
# ___ c __ ?
#     __ ? !_ ' '
#         __ ? __ st___.a.._lo..
#             key _ 'lower'
#         ____ ? __ st___.a.._u..
#             key _ 'upper'
#         ____
#             key _ 'other'
#         __ ? no. __ ?
#             c.... ?| _ se.    # se. we'll insert the value into
#
#         c... ?|.a.. ?
# ___ cat __ ?
#     print _*|?|;', ''.j.. c...|ca.|
#
# # how many times each character occurred in a string:
# # We can simplify this a bit using setdefault:
# text _ 'Some long text'
#
# categories _   # dict
# ___ c __ ?
#     __ ? !_ ' '
#         __ ? __ st___.a.._l.
#             key _ 'lower'
#         ____ ? __ st___.a.._u.
#             key _ 'upper'
#         ____
#             key _ 'other'
#         ca___.s__d___ ke. se.  .ad. ?
#
# ___ cat __ ?
#     print _*|?|:', ''.j.. c...|?
#
# # how many times each character occurred in a string:
# #
# # Just to clean things up a but more, let's create a small utility function that will r_ the category key:
# text _ 'Some long text'
#
# ___ cat_key c
#     __ ? __ ' '
#         r_ N...
#     ____ ? __ st___.a.._lo..
#         r_ 'lower'
#     ____ ? __ st___.a.._up..
#         r_ 'upper'
#     ____
#         r_ 'other'
#
# categories _  # dict
# ___ c __ ?
#     key _ cat_key ?
#     __ ?
#         c___.s_d... ke. se.  .ad. ?
#
# ___ cat __ ?
#     print _*|?|;* ''.j... c...|?
#
# # how many times each character occurred i_ a st___:
# #
# # i_ you are not a fan of using i_...el__... i_ the cat_key function we could do it this way as well
# text _ 'Some long text'
#
# ___ cat_key c
#     categories _ ' ': N...,
#                  st___.a.._lo. 'lower',
#                  st___.a.._up. 'upper'
#     ___ key __ ?
#         __ ? __ ke.
#             r_ c..|ke.|
#     ____
#         r_ 'other'
#
# cat_key 'a'  cat_key 'A'  cat_key '!'  cat_key ' '
#
# categories _  # dict
# ___ c __ text
#     key _ cat_key ?
#     __ key
#         c____.s__d__ ke. se.  .add ?
#
# ___ cat __ categories:
#     print _* ? ''.j... c... ?