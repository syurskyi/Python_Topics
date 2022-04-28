#
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
#
#     left_padding width//2 + 1
#     i 1
#
#     diff 2
#     j 1
#     lines    # list
#     w.... i > 0
#         space_before ? - i)//2
#         spaces ' ' * ?
#         line _*? S.. * ? ?
#         y.. ?
#         #line = f"{STAR * i:>{left_padding}}"
#         #yield line
#         l.. +_ d.. - j
#         i +_ ?
#
#         __ i __ ?
#             d.. -2
#             j -1
#
#
# __ _______ __ _______
#
#     _______ a__
#
#
#     ap a__.A.. "rhombus generator"
#
#     ?.a.. "-w","--width" t..=i.. r.._T.. h.._"width of rhombus"
#
#     args vars ?.p..
#     width ? "width"
#     ? ?
#
#
#
#
#
