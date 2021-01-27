from xmas import generate_xmas_tree

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


def test_height_xmas_tree():
    a__ len(generate_xmas_tree().split('\n')) == 10  # default arg
    a__ len(generate_xmas_tree(5).split('\n')) == 5
    a__ len(generate_xmas_tree(20).split('\n')) == 20


def test_num_stars_used():
    a__ generate_xmas_tree(3).count('*') == 9
    a__ generate_xmas_tree(5).count('*') == 25
    a__ generate_xmas_tree(20).count('*') == 400


def test_outputs():
    actual_tree = generate_xmas_tree().strip('\n').split('\n')
    expected_tree = default_tree.strip('\n').split('\n')
    for i, j in zip(actual_tree, expected_tree):
        a__ i.rstrip() == j.rstrip()

    actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
    expected_tree = smaller_tree.strip('\n').split('\n')
    for i, j in zip(actual_tree, expected_tree):
        a__ i.rstrip() == j.rstrip()