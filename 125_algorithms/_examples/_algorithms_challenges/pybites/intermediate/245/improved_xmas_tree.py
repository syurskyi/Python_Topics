import math

STAR = "+"
LEAF = "*"
TRUNK = "|"


def generate_improved_xmas_tree(rows=10):
   """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
      for given rows of leafs (default 10).
      For more information see the test and the bite description"""


   xmas_tree = []
   max_length = rows * 2 -1

   for i in range(rows + 1):
      if i == 0:
         xmas_tree.append(STAR.center(max_length).rstrip())
         continue

      leaf_count = i * 2 -1
      xmas_tree.append((leaf_count * LEAF).center(max_length).rstrip())

   for i in range(2):
      if rows % 2 != 0:
         product = math.ceil(max_length / 2)
      else:
         product = math.floor(max_length / 2) + 2

      xmas_tree.append((product * TRUNK).center(max_length))
   
   return "\n".join(xmas_tree)

if __name__ == "__main__":
  print(generate_improved_xmas_tree())