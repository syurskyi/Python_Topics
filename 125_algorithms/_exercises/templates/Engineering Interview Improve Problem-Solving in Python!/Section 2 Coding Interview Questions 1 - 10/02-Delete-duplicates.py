# # input = [1, 2, 1, 4, 5, 6, 6] ... output [1,2,4,5,6]
#
# ___ remove_duplicates l  # worst case [1,2,4,5,6]
#     result _   # dict
#     __ val __ ? # n times
#         __ no. ? __ ? # 1, 2, 3, 4 ... n - 1 # Balanced tree as a result  we would get n * log n
#             ?|? _ 1 #(n * n - 1) /2 = O(n squared)
#     r_ li.. ?.k.. # n times 1 (dont count colisions)
#
# print ? 1, 2, 1, 4, 5, 6, 6
#