# STAR '*'
#
# ___ gen_rhombus width
#     """Create a generator that yields the rows of a rhombus row
#        by row. So if width = 5 it should generate the following
#        rows one by one:
#
#        gen = gen_rhombus(5)
#        for row in gen:
#            print(row)
#
#         output:
#           *
#          ***
#         *****
#          ***
#           *
#     """
#
#     stars   # list
#     ___ line __ r.. ? + 1
#         ?.a.. ? * '*')
#
#     count 0
#     ___ line __ ?
#         __ ? % 1 __ 0
#             ?.r.. ?
#             ? +_ 1
#
#     output line.c.. l.. ? -1 ' ' ___ ? __ ?
#
#     r.. ? + l.. r.. ? 1|