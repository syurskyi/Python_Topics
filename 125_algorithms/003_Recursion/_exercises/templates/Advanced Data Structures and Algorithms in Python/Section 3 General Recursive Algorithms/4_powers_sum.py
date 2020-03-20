# ______ numpy __ np
#
# ___ naive A, n
#     result _ ?.zeros_like ?
#     power _ A
#     ___ i __ ra.. 1 ?+1
#         r.. +_ p..
#         p.. _ ?.matmul p.. ? % 666013
#         r.. %_ 666013
#     r_ ?
#
# ___ optimal A n
#     # n _ 2k    _> S _ (I+A^k)(A+...+A^k)
#     # n _ 2k+1  _> S _ (I+A^k)(A+...+A^k)+A^(2k+1)
#     # n _ 1 _>  _> S _ A
#     eye _ ?.e.. ?.shape 0
#     ___ inner A n
#         __ n __ 1
#             r_ A, A
#
#         A_pow_n_div2, S_n_div2 _ inner(A, n // 2)
#         A_pow_n _ ?.matmul(A_pow_n_div2, A_pow_n_div2) % 666013
#         S_n _ ?.matmul(eye + A_pow_n_div2, S_n_div2)
#         if n % 2 == 0:
#             r_ A_pow_n % 666013, S_n % 666013
#         A_pow_n _ ?.matmul(A_pow_n, A) % 666013
#         r_ A_pow_n % 666013, (S_n + A_pow_n) % 666013
#     r_ inner(A, n)[1]
#
#
#
# n _ 1000
# arr _ ?.array([[1,2],[3,4]], dtype_?.int64)
# print(naive(arr, n))
# print(optimal(arr, n))
#
# ___ i __ ra..(1, 1000):
#     assert ?.array_equal(naive(arr, i), optimal(arr, i))
