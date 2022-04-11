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

c_ Solution(o..
    ___ numTrees  n
        t [-1 ___ _ __ r..(n + 1)]
        t[0] 1
        t[1] 1
        __ n <_ 1:
            r.. t[n]
        ____
            ___ i __ r..(2, n + 1
                res 0
                ___ j __ r..(i
                    res += t[j] * t[i - 1 - j]
                t[i] res
        r.. t[n]
