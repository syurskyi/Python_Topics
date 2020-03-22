# # ((()())()) => True
# # # )())) = False
# # # (() => False
# # # )( => False
# #
# # ___ check s
# #     left _ 0
# #     ___ c __ ?
# #         __ ? __ '('
# #             l.. +_ 1
# #         ____
# #             __ l.. __ 0
# #                 r_ F..
# #             l.. -_ 1
# #     r_ l.. __ 0
# #
# # print(check("((()())())"))
# # print(check("(()()))"))
# # print(check(")("))