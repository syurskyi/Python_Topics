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


c_ TreeNode:
    ___ - , x
        val = x
        left = N..
        right = N..


c_ Solution:
    ___ rightSideView  root
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

        w.... cur_lvl:
            ret.a..(cur_lvl[-1].val)
            w.... cur_lvl:
                cur = cur_lvl.p.. 0)
                __ cur.left: nxt_lvl.a..(cur.left)
                __ cur.right: nxt_lvl.a..(cur.right)

            cur_lvl = nxt_lvl
            nxt_lvl    # list

        r.. ret