# _______ m__
#
# STAR "+"
# LEAF "*"
# TRUNK "|"
#
#
# ___ generate_improved_xmas_tree rows=10
#     """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
#        for given rows of leafs (default 10).
#        For more information see the test and the bite description"""
#
#     last_row_size =  2 * ? - 1
#
#     lines _* S..:^ ?
#
#
#
#     ___ row __ r.. ?
#         leafs 2 * (? + 1) - 1
#         line _* L.. * ?:^ l..
#         l__.a.. ?
#
#
#     last_row_size l.. l.. -1
#
#     x ?/2
#
#     __ i.. m__.f.. x % 2 __ 0
#         trunk_width i.. m__.c.. x
#     ____
#         trunk_width i.. m__.c.. x + 1
#
#
#     trunk _* T.. * t..:^ l..
#     ___ _ __ r.. 2
#         l__.a.. ?
#
#
#
#     r.. '\n'.j.. ?
#
# __ _______ __ _______
#
#     rows 50
#     print ? ?
