# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# """
# http://www.dabeaz.com/coroutines/
# """
#
# ____ c_l_ ______ c_m__
# ______ __
# ______ ___
# ______ ti..
# ______ a..
#
#
# c_ Handler o..
#     m..
#
#     ___ - successor_N..
#         _?  ?
#
#     ___ handle request
#         res _ _h.. ?
#         __ no. ?
#             _s___.h.. ?
#
#     ??.?
#     ___ _handle request
#         r_ N.. ('Must provide implementation __ subclass.')
#
#
# c_ ConcreteHandler1 H..
#
#     ___ _handle request
#         __ 0 < ? <_ 10
#             print('request @ handled __ handler 1'.f.. ?
#             r_ T..
#
#
# c_ ConcreteHandler2 H..
#
#     ___ _handle request
#         __ 10 < ? <_ 20
#             print('request @ handled __ handler 2'.f.. ?
#             r_ T..
#
#
# c_ ConcreteHandler3 H..
#
#     ___ _handle request
#         __ 20 < ? <_ 30
#             print('request @ handled __ handler 3'.f.. ?
#             r_ T..
#
#
# c_ DefaultHandler H..
#
#     ___ _handle request
#         print('end of chain, no handler ___ @'.f.. ?
#         r_ T..
#
#
# c_ Client o..
#
#     ___ -
#         handler _ C_1|
#             C_3|C_2|D..
#
#     ___ delegate requests
#         ___ request __ ?
#             h___.h.. ?
#
#
# ___ coroutine func
#     ___ start $ $$
#         cr _ func $ $$
#         ne.. ?
#         r_ ?
#     r_ st..
#
#
# ?co..
# ___ coroutine1 target
#     w___ T..
#         request _ y..
#         __ 0 < ? <_ 10
#             print('request @ handled __ coroutine 1'.f.. ?
#         ____
#             t___.se.. ?
#
#
# ?co..
# ___ coroutine2 target
#     w____ T..
#         request _ y...
#         __ 10 < ? <_ 20
#             print('request @ handled __ coroutine 2'.f.. ?
#         _____
#             t___.s.. ?
#
#
# ???
# ___ coroutine3 target
#     w___ T..
#         request _ y...
#         __ 20 < ? <_ 30
#             print('request @ handled __ coroutine 3'.f.. ?
#         ____
#             t___.s.. ?
#
#
# ??
# ___ default_coroutine
#     w____ T..
#         request _ y...
#         print('end of chain, no coroutine ___ @'.f.. ?
#
#
# c_ ClientCoroutine:
#
#     ___ -
#         target _ c_1|c_3|c_2|d_c..
#
#     ___ delegate requests
#         ___ request __ ?
#             t___.se.. ?
#
#
# ___ timeit func
#
#     ___ count $ $$
#         start _ ti__.ti__
#         res _ func $ $$
#         co__._t__ _ ti__.ti__ - st..
#         r_ ?
#     r_ ?
#
#
# ?c..m..
# ___ suppress_stdout
#     ___
#         s_o_, ___.s_o. _ ___.s_o_, o.. __.devnull, _
#         y...
#     f...
#         ___.s_o_ _ s_o_
#
#
# __ _______ __ ______
#     client1 _ C..
#     client2 _ CC..
#     requests _ [2, 5, 14, 22, 18, 3, 35, 27, 20]
#
#     c_1.de.. r..
#     print('-' * 30)
#     c_2.de.. r..
#
#     r... *_ 10000
#     client1_delegate _ ti_i. c_1.de...
#     client2_delegate _ ti_i. c_2.de...
#     w___ s_s..
#         client1_delegate r..
#         client2_delegate r..
#     # lets check which is faster
#     print(c_1_de__._ti.., c_2_de__._ti..
#
# ### OUTPUT ###
# # request 2 handled __ handler 1
# # request 5 handled __ handler 1
# # request 14 handled __ handler 2
# # request 22 handled __ handler 3
# # request 18 handled __ handler 2
# # request 3 handled __ handler 1
# # end of chain, no handler ___ 35
# # request 27 handled __ handler 3
# # request 20 handled __ handler 2
# # ------------------------------
# # request 2 handled __ coroutine 1
# # request 5 handled __ coroutine 1
# # request 14 handled __ coroutine 2
# # request 22 handled __ coroutine 3
# # request 18 handled __ coroutine 2
# # request 3 handled __ coroutine 1
# # end of chain, no coroutine ___ 35
# # request 27 handled __ coroutine 3
# # request 20 handled __ coroutine 2
# # (0.2369999885559082, 0.16199994087219238)
