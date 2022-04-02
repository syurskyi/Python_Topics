_______ p__

____ improved_xmas_tree _______ generate_improved_xmas_tree

default_tree = """
         +
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
    |||||||||||
    |||||||||||
"""
smaller_tree = """
  +
  *
 ***
*****
 |||
 |||
"""


?p__.m__.p.("size, expected", [(10, 13), (5, 8), (20, 23)])
___ test_height_xmas_tree(size, expected
    actual = l..(generate_improved_xmas_tree(size).rstrip().s..
    ... actual __ expected


?p__.m__.p.("size, expected", [(3, 9), (5, 25), (20, 400)])
___ test_num_leafs_used(size, expected
    ... generate_improved_xmas_tree(size).c.. "*") __ expected


?p__.m__.p.("size, expected", [(3, 1), (5, 1), (20, 1)])
___ test_star_used(size, expected
    ... generate_improved_xmas_tree(size).c.. "+") __ expected


?p__.m__.p.("size, expected", [(3, 6), (5, 10), (20, 42)])
___ test_trunk_used(size, expected
    ... generate_improved_xmas_tree(size).c.. "|") __ expected


___ test_outputs
    actual_tree = generate_improved_xmas_tree().strip("\n").s..("\n")
    expected_tree = default_tree.strip("\n").s..("\n")
    ___ i, j __ z..(actual_tree, expected_tree
        ... i.rstrip() __ j.rstrip()

    actual_tree = generate_improved_xmas_tree(3).strip("\n").s..("\n")
    expected_tree = smaller_tree.strip("\n").s..("\n")
    ___ i, j __ z..(actual_tree, expected_tree
        ... i.rstrip() __ j.rstrip()