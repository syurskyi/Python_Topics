"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""
__author__ 'Danyang'
# Definition for a  binary tree node
c_ TreeNode:
    ___ - , x
        val x
        left N..
        right N..

c_ Solution:
    ___ isSameTree  p, q
        """
        dfs
        :param p: TreeNode
        :param q: TreeNode
        :return: boolean
        """

        # trivial
        __ n.. p a.. n.. q:
            r.. T..

        # dfs
        ___
            __ p.val__q.val a.. isSameTree(p.left, q.left) a.. isSameTree(p.right, q.right
                r.. T..
        ______ AttributeError:
            r.. F..

        r.. F..
