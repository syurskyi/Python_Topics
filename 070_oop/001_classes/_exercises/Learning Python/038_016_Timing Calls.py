# _______ ti..
#
# c_ timer
#     ___ - ____ func
#         ____.f___ _ f___
#         ____.alltime _ 0
#
#     ___ -c ____, $ $$:
#         start   _ ti__.c...
#         result  _ ____.f___$ $$
#         elapsed _ ti__.c... - start
#         ____.all.. +_ el..
#         print('@: @.5_, @.5_' @ ____.f___. -n el.. ____.all..
#         r_ r..
#
# _t..
# ___ listcomp N
#     r_  x * 2 ___ x i_ ra.. N
#
# _t..
# ___ mapcall N
#     r_ ma. l_____ x: x * 2 ra.. N
#
#
# result _ listcomp 5                # Time for this call, all calls, return value
# listcomp(50000)
# listcomp(500000)
# listcomp(1000000)
# print(result)
# print('allTime _ @' @ listcomp.alltime)      # Total time for all listcomp calls
#
# print('')
# result _ mapcall(5)
# mapcall(50000)
# mapcall(500000)
# mapcall(1000000)
# print(result)
# print('allTime _ @' @ mapcall.alltime)       # Total time for all mapcall calls
#
# print('map/comp _ @' @ round(mapcall.alltime / listcomp.alltime, 3))
#
# import sys
#
# _t..
# ___ listcomp N
#     r_ x * 2 ___ x i_ ra.. N
# 
#
# i_ ___.ve.._in.. 0 __ 2
#     _t..
#     ___ mapcall N
#         r_ ma. l____ x x * 2), ra.. N
# e____
#     _t..
#     ___ mapcall N
#         r_ li.. ma. l____ x x * 2), ra.. N
