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
class TreeNode:
    ___ __init__(self, x
        self.val = x
        self.left = None
        self.right = None


from collections ______ defaultdict


class Solution:
    ___ findFrequentTreeSum(self, root
        """
        traverse with counter
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = defaultdict(int)
        self.traverse(root, counter)
        ret = [[], 0]
        for k, v in counter.items(
            __ v > ret[1]:
                ret[0] = [k]
                ret[1] = v
            ____ v __ ret[1]:
                ret[0].append(k)

        r_ ret[0]

    ___ traverse(self, root, counter
        __ not root:
            r_ 0

        cur = root.val
        cur += self.traverse(root.left, counter)
        cur += self.traverse(root.right, counter)
        counter[cur] += 1
        r_ cur
