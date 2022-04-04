"""
Premium Question
https://leetcode.com/problems/closest-binary-search-tree-value-ii/
"""
__author__ = 'Daniel'


c_ TreeNode(o..
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution(o..
    ___ closestKValues  root, target, k
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
        predecessors(root, target, pre)
        successors(root, target, suc)
        r.. merge(target, k, pre, suc)

    ___ predecessors  root, target, stk
        __ n.. root:
            r..

        predecessors(root.left, target, stk)
        __ root.val <_ target:
            stk.a..(root.val)
            predecessors(root.right, target, stk)

    ___ successors  root, target, stk
        __ n.. root:
            r..

        successors(root.right, target, stk)
        __ root.val > target:
            stk.a..(root.val)
            successors(root.left, target, stk)

    ___ merge  target, k, pre, suc
        ret    # list
        w.... l..(ret) < k:
            __ n.. pre:
                ret.a..(suc.pop
            ____ n.. suc:
                ret.a..(pre.pop
            ____ a..(pre[-1] - target) < a..(suc[-1] - target
                ret.a..(pre.pop
            ____
                ret.a..(suc.pop
        r.. ret