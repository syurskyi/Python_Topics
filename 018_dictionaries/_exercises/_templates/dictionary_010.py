# # -*- coding: utf-8 -*-
#
# # how many times each character occurred i_ a st___:
# text _ 'Some long text'
# counts _ di__
# ___ c i_ text:
#     key _ c.lo..  .st..
#     i_ ke.
#         counts|key| _ co__.ge. ke., 0  + 1
# print co___
#
# # how many times each character occurred i_ a st___:
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
# categories _ {}
# ___ c i_ text
#     i_ c !_ ' '
#         i_ c i_ st___.a.._l..
#             key _ 'lower'
#         el__ c i_ st___.a.._u..
#             key _ 'upper'
#         e__
#             key _ 'other'
#         i_ ke. no. i_ c...
#             c....|key| _ se.    # se. we'll insert the value into
#
#         c...|ke.|.add c
# ___ cat i_ c..
#     print _*|cat|;', ''.j.. c...|ca.|
#
# # how many times each character occurred i_ a st___:
# # We can simplify this a bit using setdefault:
# text _ 'Some long text'
#
# categories _ {}
# ___ c i_ text
#     i_ c !_ ' '
#         i_ c i_ st___.a.._l.
#             key _ 'lower'
#         el__ c i_ st___.a.._u.
#             key _ 'upper'
#         e__
#             key _ 'other'
#         ca___.s__d___ ke. se.  .add c
#
# ___ cat i_ categories
#     print _*|cat|;:', **.j.. c...|cat|
#
# # how many times each character occurred i_ a st___:
# #
# # Just to clean things up a but more, let's create a small utility function that will r_ the category key:
# text _ 'Some long text'
#
# ___ cat_key c
#     i_ c __ ' '
#         r_ N...
#     el__ c i_ st___.a.._lo..
#         r_ 'lower'
#     el__ c i_ st___.a.._up..
#         r_ 'upper'
#     e__:
#         r_ 'other'
#
# categories _ {}
# ___ c i_ text
#     key _ cat_key c
#     i_ key
#         c___.s_d... ke. se.  .add c
#
# ___ cat i_ categories
#     print _*|cat|;* **.j... c...|ca.|
#
# # how many times each character occurred i_ a st___:
# #
# # i_ you are not a fan of using i_...el__... i_ the cat_key function we could do it this way as well
# text _ 'Some long text'
#
# ___ cat_key c
#     categories _ {' ': N...,
#                  st___.a.._lo.: 'lower',
#                  st___.a.._up.: 'upper'}
#     ___ key i_ categories
#         i_ c i_ ke.
#             r_ c..|ke.|
#     e__:
#         r_ 'other'
#
# cat_key 'a'  cat_key 'A'  cat_key '!'  cat_key ' '
#
# categories _ {}
# ___ c i_ text
#     key _ cat_key c
#     i_ key
#         c____.s__d__ ke. se.  .add c
#
# ___ cat i_ categories:
#     print _* cat **.j... c... cat