# ___ maxSum arr windowSize
#     arraySize _ le. ?
#     # n must be greater than k
#     __ ? <_ ?
#         print("Invalid operation")
#         r_ -1
#
#     # Compute sum of first window of size k
#     window_sum _ su.||?|i ___ i __ ra.. ?
#     max_sum _ ?
#     # Compute sums of remaining windows by
#     # removing first element of previous
#     # window and adding last element of
#     # current window.
#     ___ i __ ra.. a.. - w..
#         window_sum _ w.. - a.. ? + a.. ? + w..
#         max_sum _ ma. w.. m..
#
#     r_ ?
#
#
# arr _  1, 2, 100, -1, 5
# # maximum sum should be 104 => 100 + -1 + 5
# answer _ ? ? 3
# print ?
