"""
Premium Question
https://leetcode.com/problems/closest-binary-search-tree-value-ii/
"""
__author__ = 'Daniel'


class TreeNode(object):
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution(object):
    ___ closestKValues(self, root, target, k):
        """
        consider the predecessors and successors of the closest node to the target
        Like merge in the merge sort, compare and pick the closest one to the target and put it to the result list

        Inorder traversal gives us sorted predecessors, whereas reverse-inorder traversal gives us sorted successors

        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        pre    # list
        suc    # list
        self.predecessors(root, target, pre)
        self.successors(root, target, suc)
        r.. self.merge(target, k, pre, suc)

    ___ predecessors(self, root, target, stk):
        __ n.. root:
            r..

        self.predecessors(root.left, target, stk)
        __ root.val <= target:
            stk.a..(root.val)
            self.predecessors(root.right, target, stk)

    ___ successors(self, root, target, stk):
        __ n.. root:
            r..

        self.successors(root.right, target, stk)
        __ root.val > target:
            stk.a..(root.val)
            self.successors(root.left, target, stk)

    ___ merge(self, target, k, pre, suc):
        ret    # list
        while l..(ret) < k:
            __ n.. pre:
                ret.a..(suc.pop())
            ____ n.. suc:
                ret.a..(pre.pop())
            ____ abs(pre[-1] - target) < abs(suc[-1] - target):
                ret.a..(pre.pop())
            ____:
                ret.a..(suc.pop())
        r.. ret