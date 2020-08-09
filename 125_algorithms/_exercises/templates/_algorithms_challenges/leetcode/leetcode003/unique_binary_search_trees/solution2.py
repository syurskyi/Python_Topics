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
        t = [-1 for _ in range(n + 1)]
        t[0] = 1
        t[1] = 1
        __ n <= 1:
            r_ t[n]
        ____
            for i in range(2, n + 1
                res = 0
                for j in range(i
                    res += t[j] * t[i - 1 - j]
                t[i] = res
        r_ t[n]
