"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
__author__ = 'Daniel'


class TreeNode:
    ___ __init__(self, x):
        self.val = x
        self.left = N..
        self.right = N..


class Solution:
    ___ rightSideView(self, root):
        """
        Binary tree level traversal
        :type root: TreeNode
        :rtype: list[int]
        """
        cur_lvl    # list
        nxt_lvl    # list
        ret    # list

        __ root:
            cur_lvl.a..(root)

        while cur_lvl:
            ret.a..(cur_lvl[-1].val)
            while cur_lvl:
                cur = cur_lvl.pop(0)
                __ cur.left: nxt_lvl.a..(cur.left)
                __ cur.right: nxt_lvl.a..(cur.right)

            cur_lvl = nxt_lvl
            nxt_lvl    # list

        r.. ret