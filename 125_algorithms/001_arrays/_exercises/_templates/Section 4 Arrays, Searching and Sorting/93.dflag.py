# ___ dflag myarray
#     print("given array:"?
#     n _ len(?)
#     zeroIndex _ 0; twoIndex _ n - 1
#     currentIndex _ 0
#     w__ ? <_ t..
#         # print "CURIndex:",currentIndex,"MYARRAY:",myarray,"ZEROIndex:",zeroIndex,"TWOIndex:",twoIndex
#         __ ?|? __ 0
#             __ ? > ?
#                 # print "currentIndex:",currentIndex,"is > then zeroIndex:",zeroIndex
#                 # print "myarray[currentIndex:",currentIndex,"] is 0, so exchanging myarray[",zeroIndex,"] and myarray[",currentIndex,"]:",myarray[zeroIndex], "with", myarray[currentIndex]
#                 ?|? ?|? _ ?|? ?|?
#                 # print "moving zeroindex from",zeroIndex,"to",zeroIndex+1
#                 ? +_ 1
#             ____
#                 c.. +_ 1
#                 ? +_ 1
#
#         ____ ?|c.. __ 2
#             __ ? < t..
#                 # print "currentIndex:",currentIndex,"is < then twoIndex:",twoIndex
#                 # print "myarray[currentIndex:",currentIndex,"] is 2, so exchanging myarray[",twoIndex,"] and myarray[",currentIndex,"]:",myarray[twoIndex], "with", myarray[currentIndex]
#                 ?|? ?|? _ ?|? ?|?
#                 # print "moving twoIndex from",twoIndex,"to",twoIndex-1
#                 ? -_ 1
#             ____
#                 b..
#         ____
#             currentIndex +_ 1
#     print(?, '\n')
#     r_ ?
#
# __ _____ __ _______
#     # dflag([0,1,2])
#     # dflag([0,2,1])
#     # dflag([2, 0, 1, 0, 2])
#     dflag([2, 0, 1, 0, 2, 1, 2, 2, 1, 1])
#     # dutchflag([2, 1, 2, 1, 2, 0])
#     # dutchflag([0, 0, 1, 2, 2, 2, 0, 0, 0])
