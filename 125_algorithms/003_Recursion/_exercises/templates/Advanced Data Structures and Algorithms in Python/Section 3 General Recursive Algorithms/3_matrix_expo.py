# c_ Matrix
#
#     ___ - rows cols
#         mat _   # list
#         ?  ?
#         ?  ?
#         ___ i __ ra.. r..
#             m__.ap.. 0 * c..
#
#     ___ __mul__ other
#         as.. cols __ ?.r..
#         result _ M.. r.. ?.c..
#         ___ k __ ra..  ?.r..
#             ___ i __ ra.. r..
#                 ___ j __ ra.. ?.c..
#                     r__.m.. ? ? +_ m.. ? ? * ?.m.. ? ?
#         r_ ?
#
#     ___ __mod__ mod
#         result _ M.. r.. c..
#         ___ i __ ra..  r..
#             ___ j __  ra..  c..
#                 r___.m.. ? ? _ m.. ? ? % ?
#         r_ ?
#
#     ___ __pow__ power modulo_666013
#         as.. r.. __ c..
#         __ ? __ 0
#             ret _ M.. r.. c..
#             ___ i __ ra..  c..
#                 ?.m.. ? ? _ 1
#             r_ ?
#
#         half_power _ ____ ** p.. // 2
#         __ p.. % 2 __ 0
#             r_ ? * ? % m..
#         r_ ? * ? * ____ % m..
#
#     ___ -s
#         result _ ''
#         ___ i __ ra..  r..
#             ___ j __ ra.. c..
#                 r.. +_ st. m.. ? ? + '\t'
#             r.. +_ '\n'
#         r_ ?
#
#
# mat _ ?(2, 2)
# ?.mat _ [[1, 1], [1, 0]]
# print(mat)
# print(mat * mat)
# print(mat * mat * mat)
# print(mat * mat * mat * mat)
# print(mat ** 1000000000000000000) # 10 ** 18, instant execution time
