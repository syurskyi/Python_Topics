____ xmas _______ generate_xmas_tree

default_tree = """
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
"""
smaller_tree = """
  *
 ***
*****
"""


___ test_height_xmas_tree():
    ... l..(generate_xmas_tree().split('\n')) __ 10  # default arg
    ... l..(generate_xmas_tree(5).split('\n')) __ 5
    ... l..(generate_xmas_tree(20).split('\n')) __ 20


___ test_num_stars_used():
    ... generate_xmas_tree(3).c.. '*') __ 9
    ... generate_xmas_tree(5).c.. '*') __ 25
    ... generate_xmas_tree(20).c.. '*') __ 400


___ test_outputs():
    actual_tree = generate_xmas_tree().strip('\n').split('\n')
    expected_tree = default_tree.strip('\n').split('\n')
    ___ i, j __ zip(actual_tree, expected_tree):
        ... i.rstrip() __ j.rstrip()

    actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
    expected_tree = smaller_tree.strip('\n').split('\n')
    ___ i, j __ zip(actual_tree, expected_tree):
        ... i.rstrip() __ j.rstrip()