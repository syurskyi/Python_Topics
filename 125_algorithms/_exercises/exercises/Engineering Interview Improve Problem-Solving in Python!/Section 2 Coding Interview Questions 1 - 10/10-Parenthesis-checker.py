# # ((()())()) => True
# # )())) = False
# # (() => False
# # )( => False
#
# ___ check s
#     left _ 0
#     ___ c __ ?
#         __ c __ '(':
#             ? +_ 1
#         ____
#             __ ? __ 0
#                 r_ F..
#             ? -_ 1
#     r_ ? __ 0
#
# print(?("((()())())"
# print(?("(()()))"
# print(?(")(")