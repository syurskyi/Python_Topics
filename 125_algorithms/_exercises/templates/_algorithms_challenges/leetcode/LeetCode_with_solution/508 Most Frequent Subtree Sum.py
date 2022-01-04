#!/usr/bin/python3
"""
Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values formed by
the subtree rooted at that node (including the node itself). So what is the most
frequent subtree sum value? If there is a tie, return all the values with the
highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in
any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit
signed integer.
"""


# Definition for a binary tree node.
c_ TreeNode:
    ___ - , x):
        val = x
        left = N..
        right = N..


____ collections _______ defaultdict


c_ Solution:
    ___ findFrequentTreeSum(self, root):
        """
        traverse with counter
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = defaultdict(i..)
        traverse(root, counter)
        ret = [[], 0]
        ___ k, v __ counter.i..:
            __ v > ret[1]:
                ret[0] = [k]
                ret[1] = v
            ____ v __ ret[1]:
                ret[0].a..(k)

        r.. ret[0]

    ___ traverse(self, root, counter):
        __ n.. root:
            r.. 0

        cur = root.val
        cur += traverse(root.left, counter)
        cur += traverse(root.right, counter)
        counter[cur] += 1
        r.. cur
