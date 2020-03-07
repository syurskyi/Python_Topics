# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://peter-hoffmann.com/2010/extrinsic-visitor-pattern-python-inheritance.html
#
# *TL;DR80
# Separates an algorithm from an object structure on which it operates.
# """
#
#
# c_ Node o...
#     p..
#
#
# c_ A N..
#     p..
#
#
# c_ B N..
#     p..
#
#
# c_ C A, B
#     p..
#
#
# c_ Visitor o..
#
#     ___ visit node $ $$
#         meth _ N..
#         ___ cls __ ?. -c. -m
#             meth_name _ 'visit_' + ?. -n
#             meth = ge.. ? ? N...
#             __ ?
#                 b...
#
#         __ no. ?
#             meth _ g_v..
#         r_ ? node $  $$
#
#     ___ generic_visit node $ $$
#         print('generic_visit ' + ?. -c. -n
#
#     ___ visit_B node $  $$
#         print'visit_B ' + ?. -c. -n
#
#
# a = A()
# b = B()
# c = C()
# visitor = V..
# ?.v..(a)
# ?.v..(b)
# ?.v..(c)
#
# ### OUTPUT ###
# # generic_visit A
# # visit_B B
# # visit_B C
