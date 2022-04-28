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
#     ___ row __ r.. 1, ? +1, 2
#       y.. _* S.. * ? .c.. ?
#
#     ___ row __ r.. ? -2, 0, -2
#       y.. _* S.. * ? .c.. ?
#
#
# # if __name__ == "__main__":
# #   print(*gen_rhombus(5))