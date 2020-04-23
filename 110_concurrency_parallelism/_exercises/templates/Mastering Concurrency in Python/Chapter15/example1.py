# # ch15/example1.py
#
# ______ ___
#
# print _*Reference count when direct-referencing: |___.g_f_ 7 .
#
# a _ [7]
# print _*Reference count when referenced once: |___.g_f_(a .
#
# b _ a
# print _*Reference count when referenced twice: |___.g_f_(a .
#
# ###########################################################################
#
# a 0 _ 8
# print _*Variable a after a is changed: |a .')
# print _*Variable b after a is changed: |b .')
#
# print('Finished.')
