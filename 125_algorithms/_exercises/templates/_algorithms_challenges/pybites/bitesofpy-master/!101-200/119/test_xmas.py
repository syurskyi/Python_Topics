from xmas ______ generate_xmas_tree

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


___ test_height_xmas_tree(
    assert le.(generate_xmas_tree().split('\n')) __ 10  # default arg
    assert le.(generate_xmas_tree(5).split('\n')) __ 5
    assert le.(generate_xmas_tree(20).split('\n')) __ 20


___ test_num_stars_used(
    assert generate_xmas_tree(3).count('*') __ 9
    assert generate_xmas_tree(5).count('*') __ 25
    assert generate_xmas_tree(20).count('*') __ 400


___ test_outputs(
    actual_tree = generate_xmas_tree().strip('\n').split('\n')
    expected_tree = default_tree.strip('\n').split('\n')
    ___ i, j in zip(actual_tree, expected_tree
        assert i.rstrip() __ j.rstrip()

    actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
    expected_tree = smaller_tree.strip('\n').split('\n')
    ___ i, j in zip(actual_tree, expected_tree
        assert i.rstrip() __ j.rstrip()