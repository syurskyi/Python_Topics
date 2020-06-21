# ______ t..
#
# NUM_REPETITIONS _ 100
#
# SETUP_CODE _ "from random import shuffle"
#
# # First test case - Insertion Sort
#
# ___ insertion_sort lst
#     ___ i __ ra.. 1 le. ?
#         elem_selected _ ?|?
#
#         w__ i > 0 an. ? < ?|?-1
#             ?|? _ ?|?-1
#             ? -_ 1
#
#         ?|? _ ?
#
#
# test_code_1 _ '''
#
# a _ [i for i in range(1000)]
#
# shuffle(a)
#
# insertion_sort(a)
#
# '''
#
# print("\n==> Testing Insertion Sort")
#
# time _ t__.t.. _1 s.. n.. g..
#
# print("Total time to sort the list:" ?
# print("Average time per repetition:"  t../N..
#
#
# # Second test case - Merge Sort
#
# ___ merge_sort lst
#
#     __ le.(?) __ 0 o. le.(?) __ 1
#         r_ ?
#     else:
#         middle_index _ le.(?)//2
#
#         left _ ? ?|;?
#         right _ ? ?|?;
#
#         r_ ? ? ?
#
#
# ___ merge left_half right_half
#
#     __ no. ? o. no. ?
#         r_ ? o. ?
#
#     result _    # list
#     i j _ 0 0
#
#     w__ T..
#
#         __ ?|? < right_half|?
#             ?.ap.. ?|?
#             i +_ 1
#         ____
#             ?.ap..?|?
#             j +_ 1
#
#         __ i __ le. ? o. j __ le. ?
#             ?.ex.. ?|?; o. ?|?;
#             b..
#
#     r_ ?
#
#
# test_code_2 _ '''
#
# b _ [i for i in range(1000)]
#
# shuffle(b)
#
# merge_sort(b)
#
# '''
#
# print("\n==> Testing Merge Sort")
#
# time _ t__.t.. _2, s.. n.. g..
#
# print("Total time to sort the list:", time)
# print("Average time per repetition:", time/NUM_REPETITIONS)
#
#
# # Third test case - Quicksort
#
# ___ quicksort lst low high
#     __ ? < ?
#         pivot_index _ ?|? ? ?
#
#         ? ? ? ?-1
#         ? ? ?+1 ?
#
# ___ partition lst low high
#     pivot _ ?|?
#
#     i _ ? - 1
#
#     ___ j __ ra.. ? ?
#         __ ?|? <_ ?
#             ? +_ 1
#             ?|? ?|? _ ?|? ?|?
#
#     ?+1 ?|? _ ?|? ?|?+1
#     r_ ?+1
#
# test_code_3 _ '''
#
# c _ [i for i in range(1000)]
#
# shuffle(c)
#
# quicksort(c, 0, len(c)-1)
#
# '''
#
# print("\n==> Testing Quicksort")
#
# time _ t__.t.. _3, s.. n.. g..
#
# print("Total time to sort the list:" ?
# print("Average time per repetition:" t../N..
