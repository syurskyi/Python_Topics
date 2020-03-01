# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# *References:
# http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python
#
# *TL;DR80
# Decouples an abstraction from its implementation.
# """
#
#
# # ConcreteImplementor 1/2
# c_ DrawingAPI1 o..
#
#     ___ draw_circle x y radius
#         print('API1.circle at @:@ radius @'.f.. ?  ?  ?
#
#
# # ConcreteImplementor 2/2
# c_ DrawingAPI2 o..
#
#     ___ draw_circle x y radius
#         print('API2.circle at @:@ radius @'.f.. ?  ?  ?
#
#
# # Refined Abstraction
# c_ CircleShape o..
#
#     ___ - x y radius drawing_api
#         _?  ?
#         _?  ?
#         _?  ?
#         _?  ?
#
#     # low-level i.e. Implementation specific
#     ___ draw
#         _d_a_.d_c.. _x _y _r..
#
#     # high-level i.e. Abstraction specific
#     ___ scale pct
#         _radius *_ ?
#
#
# ___ main
#     shapes = |
#         CS_(1, 2, 3, D_1
#         CS_(5, 7, 11, D_2
#     )
#
#     ___ shape in ?
#         ?.s.. 2.5
#         ?.d..
#
#
# __ ______ __ ______
#     ?
#
# ### OUTPUT ###
# # API1.circle at 1:2 radius 7.5
# # API2.circle at 5:7 radius 27.5
