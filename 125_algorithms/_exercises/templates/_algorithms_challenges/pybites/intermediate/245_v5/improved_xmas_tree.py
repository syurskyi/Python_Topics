# STAR "+"
# LEAF "*"
# TRUNK "|"
#
#
# ___ generate_improved_xmas_tree rows=10
#     """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
#        for given rows of leafs (default 10).
#        For more information see the test and the bite description"""
#     width rows * 2 - 1
#     out _* S..:^ ?
#     ___ n __ r.. ?
#         >.a.. _* L.. * (n * 2 + 1^ w..
#     trunk T.. * (rows + (1 __ ? % 2 __ 0 ____ 0
#     out.a.. _* ?:^ w..
#     out.a.. _* ?:^ w..
#     r.. '\n'.j.. ?
