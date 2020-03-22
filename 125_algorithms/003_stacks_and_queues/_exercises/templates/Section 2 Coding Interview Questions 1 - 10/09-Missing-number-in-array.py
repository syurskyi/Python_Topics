# # [1,2,3,5,6] => 4
# ___ missing_number l
#     ___ i __ ra.. 1 le. ? + 1 #n
#         __ i !_ ?|? - 1
#             r_ ?
#     r_ -1
#
# ___ missing_number_r l start end    #l, 3, 5
#     __ ? __ ?
#         r_ ? + 1
#     index_middle _ in. ? + ?| / 2 # 3 + 5 / 2 = 4
#     __ ?|? __ ? + 1
#         _r ? ? + 1 e..
#     ____
#         _r ? s.. i.. - 1
#
# print(?([1,2,3,5,6],0,5))