# ___ expressions expr
#     __ ? 0 __ '('
#         ? : _ ? 1:
#         result _ terms ?
#         ? : _ ? 1:
#         r_ ?
#     result _ ? 0
#     ? : _ ? 1:
#     r_ fl. ?
#
# ___ factors expr
#     result _ ? ?
#     w___ ? 0 __ '*/'
#         __ ? 0 __ '*'
#             ? : _ ? 1:
#             r.. *_ e.. ?
#         ____
#             ? : _ ? 1:
#             r.. /_ e.. ?
#     r_ ?
#
# ___ terms expr
#     result _ ? ?
#     w___ ? 0 __ '+-'
#         __ ? 0 __ '+'
#             ? : _ ? 1:
#             r... +_ f.. ?
#         ____
#             ? : _ ? 1:
#             r.. -_ f.. ?
#     r_ ?
#
# print(terms(list('4+2*(3-1).')))