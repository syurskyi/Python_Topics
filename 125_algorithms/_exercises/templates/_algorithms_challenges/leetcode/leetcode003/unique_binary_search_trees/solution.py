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

c_ Solution(o..):
    ___ numTrees  n):
        """
        :type n: int
        :rtype: int
        """
        t = [-1 ___ _ __ r..(n + 1)]
        r.. num_trees_aux(n, t)

    ___ num_trees_aux  n, t):
        __ n __ 0 o. n __ 1:
            r.. 1
        ____ t[n] != -1:
            r.. t[n]
        ____:
            res = 0
            ___ i __ r..(n):
                res += num_trees_aux(i, t) * \
                    num_trees_aux(n - 1 - i, t)
            t[n] = res
            r.. res
