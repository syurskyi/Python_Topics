#!/usr/bin/python3
"""
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:

Return its preorder traversal as: [1,3,5,6,2,4].

Note:
Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
c_ Node:
    ___ - , val, children
        val = val
        children = children


____ t___ _______ List


c_ Solution:
    ___ preorder  root: "Node") __ List[i..]:
        """
        reversely add the children to stk
        """
        ret    # list
        __ n.. root:
            r.. ret

        stk = [root]
        w.... stk:
            cur = stk.pop()
            ret.a..(cur.val)
            ___ c __ r..(cur.children
                stk.a..(c)

        r.. ret
