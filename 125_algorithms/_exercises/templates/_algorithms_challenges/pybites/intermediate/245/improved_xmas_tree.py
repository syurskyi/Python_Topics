_______ m__

STAR = "+"
LEAF = "*"
TRUNK = "|"


___ generate_improved_xmas_tree(rows=10
   """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
      for given rows of leafs (default 10).
      For more information see the test and the bite description"""


   xmas_tree    # list
   max_length = rows * 2 -1

   ___ i __ r..(rows + 1
      __ i __ 0:
         xmas_tree.a..(STAR.center(max_length).rstrip
         _____

      leaf_count = i * 2 -1
      xmas_tree.a..((leaf_count * LEAF).center(max_length).rstrip

   ___ i __ r..(2
      __ rows % 2 != 0:
         product = m__.ceil(max_length / 2)
      ____:
         product = m__.f..(max_length / 2) + 2

      xmas_tree.a..((product * TRUNK).center(max_length))
   
   r.. "\n".j..(xmas_tree)

__ _______ __ _______
  print(generate_improved_xmas_tree