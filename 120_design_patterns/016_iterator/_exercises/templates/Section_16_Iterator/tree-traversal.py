# c_ Node
#   ___ -  value, left_N... right_N...
#     r  r
#     l  l
#     v  v
#
#     parent _ N...
#
#     __ l___
#       l___.p.. _ ?
#     __ r____
#       r____.p.. _ ?
#
#   ___ -i
#     r_ IOI.. ?
#
#
# c_ InOrderIterator
#   ___ -  root
#     root _ current _ root
#     yielded_start _ F..
#     w____ c___.l___
#       c___ _ c___.l___
#
#   ___ -n
#     __ no. y_s..
#       y_s.. _ T..
#       r_ c___
#
#     __ c___.r____
#       c___ _ c___.r____
#       w____ c___.l___
#         c___ _ c___.l___
#       r_ c___
#     ____
#       p _ c___.p..
#       w____ p an. c___ __ p.r____
#         c___ _ p
#         p _ p.p..
#       c___ _ p
#       __ c___
#         r_ c___
#       ____
#         r_ S...
#
# ___ traverse_in_order root
#   ___ traverse c___
#     __ c___.l___
#       ___ l___ __ tr.. c___.l___
#         y... l___
#     y... c___
#     __ c___.r____
#       ___ r____ __ tr.. c___.r____
#         y... r____
#   ___ node __ tr.. ?
#     y... ?
#
#
#
# __ _______ __ ______
#   #   1
#   #  / \
#   # 2   3
#
#   # in-order 213
#   # preorder 123
#   # postorder 231
#
#   root _ N..(1,
#               N..(2),
#               N..(3))
#
#   it _ it.. ?
#
#   print ne.. ? .v.. ___ x __ ra.. 3
#
#   ___ x __ r..
#     print ?.v..
#
#   ___ y __ t_i_o.. r..
#     print ?.v..