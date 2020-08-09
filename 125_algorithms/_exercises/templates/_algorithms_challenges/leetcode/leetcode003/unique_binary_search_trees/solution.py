"""
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

class Solution(object
    ___ numTrees(self, n
        """
        :type n: int
        :rtype: int
        """
        t = [-1 for _ in range(n + 1)]
        r_ self.num_trees_aux(n, t)

    ___ num_trees_aux(self, n, t
        __ n __ 0 or n __ 1:
            r_ 1
        ____ t[n] != -1:
            r_ t[n]
        ____
            res = 0
            for i in range(n
                res += self.num_trees_aux(i, t) * \
                    self.num_trees_aux(n - 1 - i, t)
            t[n] = res
            r_ res
