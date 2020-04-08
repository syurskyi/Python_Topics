# print("Algorithms file loaded")
#
# ___ quicksort arr
#     __ le. ? < 2
#         r_ ?
#     ____
#         pivot _ ?|-1
#         smaller equal larger _   # lists
#         ___ num __ ?
#             __ ? < p..
#                 s__.ap.. ?
#             ____ ? __ p..
#                 e__.ap.. ?
#             ____
#                 l__.ap.. ?
#         r_ ? ? + ? + ?|?
#
# ___ merge_sorted arr1 arr2
#     sorted_arr _   # list
#     i j _ 0 0
#     w___ i < le.(?) an. j < le. ?
#         __ ?|? < ?|?
#             s__.ap.. ?|?
#             ? +_ 1
#         ____
#             s__.ap.. ?|?
#             j +_ 1
#     w___ i < le. ?
#         s__.ap.. ?|?
#         i +_ 1
#     w___ j < le. ?
#         s__.ap.. ?|?
#         j +_ 1
#     r_ ?
#
# ___ mergesort ?
#     __ le. ? < 2
#         r_ ?|;
#     ____
#         middle _ le. ? //2
#         l1 _ ? ?|;?
#         l2 _ ? ?|?;
#         r_ ? ? ?
#
# ___ bubblesort arr
#     swap_happened _ T..
#     w___ ?
#         s.. _ F..
#         ___ num __ ra.. le. ?|-1
#             __ ?|? > ?|?+1
#                 s.. _ T..
#                 ?|? ?|?+1 _ ?|?+1 ?|?
