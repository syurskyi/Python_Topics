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
#     stars line * 2 - 1) * '*' ___ ? __ r.. ? - 1
#     stacked line.c.. l.. ? -1 , ' ' ___ ? __ s? 1|
#     stacked_rev item ___ ? __ r.. ?
#     r.. ? + ? 1|