# _______ m__
#
# STAR "+"
# LEAF "*"
# TRUNK "|"
#
#
# ___ generate_improved_xmas_tree rows=10
#    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
#       for given rows of leafs (default 10).
#       For more information see the test and the bite description"""
#
#
#    xmas_tree    # list
#    max_length rows * 2 -1
#
#    ___ i __ r.. r.. + 1
#       __ ? __ 0
#          x__.a.. S__ .c.. ? .r..
#          _____
#
#       leaf_count ? * 2 -1
#       x__.a.. ? * L.. .c.. m__ .r..
#
#    ___ ? __ r.. 2
#       __ r.. % 2 !_ 0
#          product m__.c.. m.. / 2
#       ____
#          product m__.f.. m.. / 2) + 2
#
#       x__.a.. ? * T__ .c.. m..
#
#    r.. "\n".j.. x__
#
# __ _______ __ _______
#   print ?